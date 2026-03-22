from voidpet_sim.core.context import BattleContext
from voidpet_sim.core.end_conditions import EndCondition
from voidpet_sim.pets import Pet
from voidpet_sim.events.event import Event
from voidpet_sim.effects import SpeedUp

from typing import List

class Simulator:
    def __init__(self, context: BattleContext, end_condition: EndCondition, events: List[Event] = []) -> None:
        self.context = context
        self.end_condition = end_condition
        self.events = events

    def next(self, pets: List[Pet]) -> Pet:
        speeds = [pet.get_speed() for pet in pets if pet.isAlive()]
        fastest = max(speeds)

        min_time = float("inf")
        mover: Pet | None = None

        # find next mover
        for pet, speed in zip(filter(lambda pet: pet.isAlive(), pets), speeds):
            remaining: float = 100.0 - pet.atb
            velocity: float = speed / fastest
            time_to_full: float = remaining / velocity

            if time_to_full < min_time:
                min_time = time_to_full
                mover = pet

        if mover is None:
            raise RuntimeError("No pet selected for turn.")

        # Second pass: advance ATB
        for pet, speed in zip(pets, speeds):
            velocity: float = speed / fastest
            pet.atb += min_time * velocity

        return mover

    def run(self) -> None:
        # kind passive
        for pet in self.context.pets:
            if pet.name == "Kind" or pet.name == "Estrangement":
                pet.apply_effect(
                    SpeedUp(1)
                )
        while not self.end_condition.should_end(self.context):
            # before turn
            mover: Pet = self.next(self.context.pets)
            if self.context.total_turns == 0:
                for pet in self.context.pets:
                    if pet.name == "Down Bad":
                        mover = pet

            mover.increment_turn()
            mover.reset_atb()
            self.context.increment_total_turns()

            # during turn
            # print(f"{self.context.total_turns},{mover.name},{mover.turn_count}")
            print(
                f"Turn {self.context.total_turns}: "
                f"{mover.name} "
                f"(pet turns: {mover.turn_count})\n"
                f"--------------------------------------"
            )
            # tick effects
            for effect in mover.effects:
                effect.on_turn_end()
            mover.remove_expired_effects()

            # resolve items
            for item in mover.items:
                item.on_turn_end(mover, self.context)

            # resolve events
            for event in self.events:
                event.try_trigger(mover, self.context)

            
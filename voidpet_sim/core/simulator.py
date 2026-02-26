from voidpet_sim.core.context import BattleContext
from voidpet_sim.core.end_conditions import EndCondition
from voidpet_sim.models.pet import Pet

from typing import List

class Simulator:
    def __init__(self, context: BattleContext, end_condition: EndCondition) -> None:
        self.context = context
        self.end_condition = end_condition

    def next(self, pets: List[Pet]) -> Pet:
        speeds = {pet: pet.get_speed() for pet in pets}
        fastest = max(speeds.values())

        min_time: float = float("inf")
        mover: Pet | None = None

        for pet in pets:
            remaining = 100.0 - pet.atb
            velocity = speeds[pet] / fastest
            time_to_full = remaining / velocity

            if time_to_full < min_time:
                min_time = time_to_full
                mover = pet

        if mover is None:
            raise RuntimeError("No pet selected for turn.")

        # Advance all ATB
        for pet in pets:
            velocity = speeds[pet] / fastest
            pet.atb += min_time * velocity

        mover.atb = 0
        return mover

    def run(self) -> None:
        while not self.end_condition.should_end(self.context):
            # before turn
            mover: Pet = self.next(self.context.pets)
            mover.increment_turn()
            self.context.increment_total_turns()

            # during turn
            print(
                f"Turn {self.context.total_turns}: "
                f"{mover.name} "
                f"(pet turns: {mover.turn_count})"
            )
            

            # end turn
            for effect in mover.effects:
                effect.on_turn_end(mover)

            mover.remove_expired_effects()
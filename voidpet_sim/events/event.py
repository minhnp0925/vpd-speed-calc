from typing import Iterable, Set
from voidpet_sim.pets import Pet
from voidpet_sim.core import BattleContext
from voidpet_sim.events.actions import Action

class Event:
    def __init__(
        self,
        actor: Pet,
        trigger_turns: Iterable[int],
        action: Action,
    ) -> None:
        self.actor = actor
        self.trigger_turns = set(trigger_turns)
        self.action = action

    def try_trigger(self, source: Pet, context: BattleContext) -> None:
        if source is self.actor and source.turn_count in self.trigger_turns:
            self.action.execute(source, context)
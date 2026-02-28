from abc import ABC, abstractmethod
from voidpet_sim.pets import Pet
from voidpet_sim.core.context import BattleContext
from voidpet_sim.events.targets import TargetSelector

from voidpet_sim.effects.base import Effect
from typing import Type

class Action(ABC):
    @abstractmethod
    def execute(self, source: Pet, context: BattleContext) -> None:
        pass

class RemoveBuffAction(Action):
    def __init__(
        self,
        target_selector: TargetSelector,
    ) -> None:
        self.target_selector = target_selector

    def execute(self, source: Pet, context: BattleContext) -> None:
        targets = self.target_selector.select(source, context)
        for pet in targets:
            pet.remove_buffs()

class RemoveDebuffAction(Action):
    def __init__(
        self,
        target_selector: TargetSelector,
    ) -> None:
        self.target_selector = target_selector

    def execute(self, source: Pet, context: BattleContext) -> None:
        targets = self.target_selector.select(source, context)
        for pet in targets:
            pet.remove_debuffs()

class ApplyEffectAction(Action):
    def __init__(
        self,
        effect_cls: Type[Effect],
        duration: int,
        target_selector: TargetSelector,
    ) -> None:
        self.effect_cls = effect_cls
        self.duration = duration
        self.target_selector = target_selector

    def execute(self, source: Pet, context: BattleContext) -> None:
        targets = self.target_selector.select(source, context)
        for pet in targets:
            pet.apply_effect(self.effect_cls(self.duration))

class KillAction(Action):
    def __init__(self, target_selector: TargetSelector) -> None:
        self.target_selector = target_selector

    def execute(self, source: Pet, context: BattleContext) -> None:
        targets = self.target_selector.select(source, context)
        for pet in targets:
            if pet.alive:
                pet.kill()
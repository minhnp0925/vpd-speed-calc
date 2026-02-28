from abc import ABC, abstractmethod
from typing import List
from voidpet_sim.pets import Pet
from voidpet_sim.core.context import BattleContext

class TargetSelector(ABC):
    @abstractmethod
    def select(self, source: Pet, context: BattleContext) -> List[Pet]:
        pass

class AllAlliesTarget(TargetSelector):
    def select(self, source: Pet, context: BattleContext) -> List[Pet]:
        return [p for p in context.pets if p.team == source.team]
    
class AllEnemiesTarget(TargetSelector):
    def select(self, source: Pet, context: BattleContext) -> List[Pet]:
        return [p for p in context.pets if p.team != source.team]
    
class SingleTarget(TargetSelector):
    def __init__(self, target: Pet) -> None:
        self.target = target

    def select(self, source: Pet, context: BattleContext) -> List[Pet]:
        return [self.target]


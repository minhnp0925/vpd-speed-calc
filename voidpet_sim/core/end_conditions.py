from abc import ABC, abstractmethod
from voidpet_sim.core.context import BattleContext
from voidpet_sim.pets import Pet

class EndCondition(ABC):
    @abstractmethod
    def should_end(self, context: BattleContext) -> bool:
        pass

class TotalTurnEndCondition(EndCondition):
    def __init__(self, max_turns: int = 50) -> None:
        self.max_turns = max_turns

    def should_end(self, context: BattleContext) -> bool:
        return context.total_turns >= self.max_turns

class PetTurnEndCondition(EndCondition):
    def __init__(self, pet: Pet, target_turns: int) -> None:
        self.pet = pet
        self.target_turns = target_turns

    def should_end(self, context: BattleContext) -> bool:
        return self.pet.turn_count >= self.target_turns
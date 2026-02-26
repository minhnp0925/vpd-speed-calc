from __future__ import annotations
from abc import ABC, abstractmethod
from voidpet_sim.models.pet import Pet


class Effect(ABC):
    def __init__(self, duration: int) -> None:
        self.duration = duration
    
    @abstractmethod
    def modify_speed(self, current_speed: float) -> float:
        pass

    def on_turn_end(self, pet: Pet) -> None:
        self.duration -= 1

    def is_expired(self) -> bool:
        return self.duration <= 0

    def is_buff(self) -> bool:
        return False

    def is_debuff(self) -> bool:
        return False

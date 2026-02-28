from __future__ import annotations
from dataclasses import dataclass, field

from typing import List
from voidpet_sim.effects.base import Effect
from voidpet_sim.items.base import Item

@dataclass
class Pet:
    name: str
    team: int
    base_speed: float
    speed_multiplier: float = 1.0

    atb: float = 0.0
    turn_count: int = 0

    effects: List[Effect] = field(default_factory=list)
    items: List[Item] = field(default_factory=list)

    def get_speed(self) -> float:
        speed = self.base_speed
        speed *= self.speed_multiplier

        for effect in self.effects:
            speed = effect.modify_speed(speed)
        speed=round(speed,3)
        # print(f"{self.name} current speed = {speed}")
        return speed

    def apply_effect(self, new_effect: Effect) -> None:
        # Non-stackable: extend duration if same type exists
        for effect in self.effects:
            if type(effect) is type(new_effect):
                effect.duration = max(effect.duration, new_effect.duration)
                return

        self.effects.append(new_effect)

    def remove_expired_effects(self) -> None:
        self.effects = [e for e in self.effects if not e.is_expired()]

    def remove_buffs(self) -> None:
        self.effects = [e for e in self.effects if not e.is_buff()]

    def remove_debuffs(self) -> None:
        self.effects = [e for e in self.effects if not e.is_debuff()]

    def remove_all_effects(self) -> None:
        self.effects.clear()

    def increment_turn(self) -> None:
        self.turn_count += 1

    def reset_atb(self) -> None:
        self.atb = 0.0

    

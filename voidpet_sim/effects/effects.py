from voidpet_sim.effects.base import Effect

class SpeedUp(Effect):
    MULTIPLIER: float = 1.3

    def modify_speed(self, current_speed: float) -> float:
        return current_speed * self.MULTIPLIER

    def is_buff(self) -> bool:
        return True

class SpeedDown(Effect):
    MULTIPLIER: float = 0.75

    def modify_speed(self, current_speed: float) -> float:
        return current_speed * self.MULTIPLIER

    def is_debuff(self) -> bool:
        return True

class TimeStop(Effect):
    MULTIPLIER: float = 2.0

    def modify_speed(self, current_speed: float) -> float:
        return current_speed * self.MULTIPLIER

    def is_debuff(self) -> bool:
        return True
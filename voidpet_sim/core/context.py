from dataclasses import dataclass
from typing import List
from voidpet_sim.pets import Pet

@dataclass
class BattleContext:
    pets: List[Pet]
    total_turns: int = 0

    def increment_total_turns(self) -> None:
        self.total_turns += 1
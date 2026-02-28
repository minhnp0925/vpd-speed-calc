from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from voidpet_sim.pets import Pet
    from voidpet_sim.core import BattleContext

class Item(ABC):
    def on_battle_start(self, pet: "Pet", context: "BattleContext") -> None:
        pass

    def on_turn_start(self, pet: "Pet", context: "BattleContext") -> None:
        pass

    def on_turn_end(self, pet: "Pet", context: "BattleContext") -> None:
        pass
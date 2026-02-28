from voidpet_sim.items.base import Item
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from voidpet_sim.pets import Pet
    from voidpet_sim.core import BattleContext

class AnxietyScarf(Item):
    def on_turn_end(self, pet: "Pet", context: "BattleContext") -> None:
        # print("Anx proc for ", pet.name, "current mult", pet.speed_multiplier)
        pet.speed_multiplier += 0.03

class RubberRingDonut(Item):
    def on_turn_end(self, pet: "Pet", context: "BattleContext") -> None:
        if pet.turn_count == 15:
            pet.speed_multiplier += 1.00

class Hyperborean(Item):
    def on_turn_end(self, pet: "Pet", context: "BattleContext") -> None:
        pet.speed_multiplier += 0.01
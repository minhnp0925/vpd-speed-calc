from voidpet_sim.models.pet import Pet
from voidpet_sim.core import *


pet1 = Pet(name="Apathy", team=1, base_speed=10)
pet2 = Pet(name="Sad", team=2, base_speed=20)

context = BattleContext([pet1, pet2])
engine = Simulator(context, TotalTurnEndCondition(20))
engine.run()
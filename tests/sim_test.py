from voidpet_sim.pets import Pet
from voidpet_sim.core import *
from voidpet_sim.effects import *
from voidpet_sim.items import *
from voidpet_sim.events import *

pets = [
    Pet("Mischief",2,54582),
    Pet("Gronk",1,43489),
]

context = BattleContext(pets)
engine = Simulator(context, TotalTurnEndCondition(30))
engine.run()
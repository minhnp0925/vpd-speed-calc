from voidpet_sim.pets import Pet
from voidpet_sim.core import *
from voidpet_sim.effects import *
from voidpet_sim.items import *
from voidpet_sim.events import *

pets = [
    Pet("Tyrant",2,61231),
    Pet("Merry",1,47959,items=[
        AnxietyScarf()
    ]),
    Pet("Wonder",1,49714,items=[
        RubberRingDonut()
    ]),
    Pet("Cringe",1,12224),
]

context = BattleContext(pets)
engine = Simulator(context, TotalTurnEndCondition(100))
engine.run()
from voidpet_sim.pets import Pet
from voidpet_sim.core import *
from voidpet_sim.effects import *
from voidpet_sim.items import *
from voidpet_sim.events import *

pets = [
    Pet("Merry",1,45809,items=[
        Hyperborean()
    ]),
    Pet("Kind",1,39339),
    Pet("Persistence",1,29196),
    Pet("Abandonment",1,13666),
    Pet("Tauron",2,53139)
]

events = [
    Event(
        actor=pets[0],
        trigger_turns=[1,4,7,10,13,16,19,22,25,28],
        action=ApplyEffectAction(
            effect_cls=SpeedDown,
            duration=1,
            target_selector=SingleTarget(pets[4])
        )
    ),
    Event(
        actor=pets[3],
        trigger_turns=[2,3,5,6,8,9],
        action=ApplyEffectAction(
            effect_cls=SpeedDown,
            duration=1,
            target_selector=SingleTarget(pets[4])
        )
    )
]

context = BattleContext(pets)
engine = Simulator(context, TotalTurnEndCondition(100),events=events)
engine.run()
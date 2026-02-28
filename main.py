from dataclasses import dataclass
from collections import Counter
from typing import List

@dataclass
class Voidpet:
    name: str
    speed: int = 1
    scaling: float = 0.0
    rrd: bool = False

class Simulator:
    def __init__(self, pets: List[Voidpet]) -> None:
        self.pets = pets
        self.speed = {}
        for pet in pets:
            self.speed[pet.name] = pet.speed
        self.atb = {}
        fastest = max(self.speed.values())
        for pet in pets:
            self.atb[pet.name] = pet.speed/fastest*100
        self.turn_count = Counter()
    
    def simulate(self, turns = 1000):
        for i in range(turns):
            min_t = float('inf')
            moving_pet = None
            # atb velocity is normalized to current fastest pet
            current_fastest = max(self.speed.values())
            
            # find the pet that will take a turn
            for pet in self.pets:
                s = 100 - self.atb[pet.name]
                v = self.speed[pet.name]/current_fastest
                t = s/v

                if t < min_t:
                    moving_pet = pet
                    min_t = t
            assert moving_pet is not None, "Can't find moving pet"
            
            # post move updates
            for pet in self.pets:
                if pet is moving_pet:
                    self.atb[pet.name] = 0
                    self.speed[pet.name] += pet.scaling*pet.speed
                    self.turn_count[pet.name] += 1
                    print(f"{i+1},{moving_pet.name},{self.turn_count[pet.name]}")
                    # print(f"Turn #{i+1}: {moving_pet.name}, turn count = {self.turn_count[pet.name]}")
                else:
                    v = self.speed[pet.name]/current_fastest
                    self.atb[pet.name] += min_t * v
    
pets = [
    Voidpet(name="Cringe", speed=12224),
    Voidpet(name="Merry", speed=47959, scaling = 0.03),
    Voidpet(name="Wonder", speed=49714),
    Voidpet(name="Salty", speed=17622),

    Voidpet(name="Tyrant", speed=61231)
]

simulator = Simulator(pets)
simulator.simulate(100)

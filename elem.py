from abc import ABC, abstractmethod
    
class Wall():
    def __init__(self, cost: float, durability: float):
        self.cost = cost
        self.durability = durability
    
    def step(self):
        print("Wall step")
        return
    
class Fence():
    def __init__(self, cost: float, durability: float):
        self.cost = cost
        self.durability = durability

    def step(self):
        print("Fence step")
        return
    
class Crop():
    def __init__(self, cost: float, growth_rate: float, hydration: float = 100.0):
        self.cost = cost
        self.growth_rate = growth_rate
        self.hydration = hydration
    
    def soak(self, water: float = 25.0):
        self.hydration += water
    
    def dry(self, sun: float = 25.0):
        self.hydration -= sun

    def is_dead(self):
        return self.hydration <= 0.0 or self.hydration >= 150.0

    def step(self):
        self.hydration += self.growth_rate
        print(f"Crop step {self.hydration}")
    


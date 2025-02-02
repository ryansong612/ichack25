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
    def __init__(self, cost: float, growth_rate: float, hydration: float = 100.0, alive: bool = True, health: float = 0):
        # self.age = age # have for growing
        self.cost = cost
        self.growth_rate = growth_rate
        self.hydration = hydration
        self.alive = alive
        self.health = health # I thresholded by Disease.disease_threshold
    
        
    def sicken(self, amount: float = 0.42): # TODO: to be determined parameter
        self.health += amount
    
    def soak(self, water: float = 25.0):
        self.hydration += water
    
    def dry(self, sun: float = 25.0):
        self.hydration -= sun

    def is_dead(self):
        return self.hydration <= 0.0 or self.hydration >= 150.0

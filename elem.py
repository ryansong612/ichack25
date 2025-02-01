from abc import ABC, abstractmethod

class CellElem(ABC):
    def __init__(self, cost: float):
        self.cost = cost
        return
    
    @abstractmethod
    def step(self):
        pass
    
class Wall(CellElem):
    def __init__(self, cost: float, durability: float):
        super().__init__(cost)
        self.durability = durability
    
    def step(self):
        print("Wall step")
        return
    
class Fence(CellElem):
    def __init__(self, cost: float, durability: float):
        super().__init__(cost)
        self.durability = durability

    def step(self):
        print("Fence step")
        return
    
class Crop(CellElem):
    def __init__(self, cost: float, age: float, growth_rate: float, alive: bool = True):
        super().__init__(cost)
        self.age = age
        self.growth_rate = growth_rate
        self.alive = alive

    def step(self):
        self.age += self.growth_rate
        print(f"Crop step {self.age}")
    


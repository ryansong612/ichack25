from abc import ABC
from typing import Tuple

class Event(ABC):
    def __init__(self, duration: int):
        self.duration = duration
        return

class Flood(Event):
    def __init__(self, duration: int, source: Tuple[int, int], flood_chance: float):
        super().__init__(duration)
        self.source = source
        self.flood_chance = flood_chance

class Drought(Event):
    def __init__(self, duration: int, drought_chance: float):
        super().__init__(duration)
        self.drought_chance = drought_chance
    
class HeatWave(Event):
    def __init__(self, duration: int, temperature: float, offset: int):
        super().__init__(duration)
        self.temperature = temperature
        self.offset = 0

class ColdSnap(Event):
    def __init__(self, duration: int, temperature: float):
        super().__init__(duration)
        self.temperature = temperature
    
class Wind(Event):
    def __init__(self, duration: int, wind_speed: float):
        super().__init__(duration)
        self.wind_speed = wind_speed

# TODO: get values from AI
class Disease(Event):
    def __init__(self, diffusion_coeff: float, infection_p: float = 0.25, healthy_threshold: float = 0.5, disease_threshold: float = 0.8):
        self.diffusion_coeff = diffusion_coeff
        self.infection_p = infection_p # chance of randomly getting infected e.g from bugs
        self.healthy_threshold = healthy_threshold
        self.disease_threshold = disease_threshold
        # 0 <= health <= self.healthy_threshold => healthy
        # self.healthy_threshold < health < self.disease_threshold => infected
        # self.disease_threshold <= health <= 1 => dead
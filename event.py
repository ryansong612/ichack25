from abc import ABC
from typing import Tuple

class Event(ABC):
    def __init__(self):
        return

class Flood(Event):
    def __init__(self, source: Tuple[int, int], rate: float, duration: int, flood_chance: float):
        self.source = source
        self.rate = rate
        self.duration = duration
        self.flood_chance = flood_chance

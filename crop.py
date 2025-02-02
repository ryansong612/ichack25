db = {
    "Revere 1839 TC": {
        "cost": 0.78,
        "yield": 359

    },
    "Dyna-Gro D56TC44": {
        "cost": 0.59,
        "yield": 312

    },
    "BH 8721VT2P": {
        "cost": 0.28,
        "yield": 228
    }
}

class Crop:
    def __init__(self, name: str, quantity_of_land: float):
        self.name = name
        self.quantity_of_land = quantity_of_land
        self.cost = db[name]["cost"]
        self.yield_ = db[name]["yield"]

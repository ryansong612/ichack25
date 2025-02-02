class Crop():
    def __init__(self, resistances):
        self.resistances = resistances

class Crop1(Crop):
    def __init__(self):
        super().__init__([0.6, 0.4, 0.7, 0.8, 0.55, 0.6])

class Crop2(Crop):
    def __init__(self):
        super().__init__([0.35, 0.6, 0.8, 0.65, 0.7, 0.45])

class Crop3(Crop):
    def __init__(self):
        super().__init__([0.65, 0.3, 0.65, 0.5, 0.65, 0.35])
from weather_to_event import weather_to_event

from crop import Crop1, Crop2, Crop3

def main(location, month, crops_initial_percentages):
    crops = list(crops_initial_percentages.keys())
    initial_percentages = [v for k,v in crops_initial_percentages.items()]
    disasters = weather_to_event(month, location)
    disasters_percentages = [int(disasters[d]["probability"]) * 0.01 for d in list(disasters.keys())]

    crop1 = Crop1()
    crop2 = Crop2()
    crop3 = Crop3()

    crop1_final = initial_percentages[0] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop1.resistances)])
    crop2_final = initial_percentages[1] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop2.resistances)])
    crop3_final = initial_percentages[2] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop3.resistances)])

    return {crops[0]: crop1_final, crops[1]: crop2_final, crops[2]: crop3_final}
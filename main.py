from weather_to_event import weather_to_event

from crop import Crop1, Crop2, Crop3

def main(location, month, crops_initial_percentages):
    crops = list(crops_initial_percentages.keys())

    yield_list = [crop['yield'] for crop in crops_initial_percentages.values()]
    proportion_list = [crop['proportion'] for crop in crops_initial_percentages.values()]
    growth_list = [crop['growth'] for crop in crops_initial_percentages.values()]

    disasters = weather_to_event(month, location)
    disasters_percentages = [int(disasters[d]["probability"]) * 0.01 for d in list(disasters.keys())]

    crop1 = Crop1()
    crop2 = Crop2()
    crop3 = Crop3()

    crop1_proportion = proportion_list[0] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop1.resistances)])
    crop2_proportion = proportion_list[1] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop2.resistances)])
    crop3_proportion = proportion_list[2] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crop3.resistances)])

    crop1_yield = yield_list[0] + crop1_proportion / (100 + proportion_list[0])
    crop2_yield = yield_list[1] + crop2_proportion / (100 + proportion_list[1])
    crop3_yield = yield_list[2] + crop3_proportion / (100 + proportion_list[2])

    crop1_growth = min(growth_list[0] + 0.25, 1)
    crop2_growth = min(growth_list[1] + 0.4, 1)
    crop3_growth = min(growth_list[2] + 0.3, 1)

    return {crops[0]: {"yield": crop1_yield, "proportion": crop1_proportion, "growth": crop1_growth}, crops[1]: {"yield": crop2_yield, "proportion": crop2_proportion, "growth": crop2_growth, crops[2]: {"yield": crop3_yield, "proportion": crop2_proportion, "growth": crop3_growth}}}
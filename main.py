from weather_to_event import weather_to_event

from crop import Crop1, Crop2, Crop3

def main(location, month, crops_initial_percentages):
    crops = list(crops_initial_percentages.keys())

    disasters = weather_to_event(month, location)
    disasters_percentages = [int(disasters[d]["probability"]) * 0.01 for d in list(disasters.keys())]

    crops = {"wheat": Crop1(), "corn": Crop2(), "rice": Crop3()}
    
    out = {}
    for crop_name, v in crops_initial_percentages.items():
        crop_proportion = v["proportion"] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crops[crop_name].resistances)])
        crop_yield = v["yield"] + crop_proportion / (100 + v["proportion"])
        crop_growth = min(v["growth"] + 0.25, 1)
        
        out[crop_name] = {"yield": crop_yield, "proportion": crop_proportion, "growth": crop_growth}

    return out
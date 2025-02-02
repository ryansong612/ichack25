from weather_to_event import weather_to_event

from crop import Crop1, Crop2, Crop3

disasters_list = [weather_to_event(month, "London") for month in range(1, 13)]

def main(location, month, crops_initial_percentages):
    crops = list(crops_initial_percentages.keys())
    disasters = disasters_list[month - 1]

    disasters_percentages = [int(disasters[d]["probability"]) * 0.01 for d in list(disasters.keys())]

    crops = {"wheat": Crop1(), "corn": Crop2(), "rice": Crop3()}
    
    out = {}
    for crop_name, v in crops_initial_percentages.items():
        crop_proportion = v["proportion"] * 1 / len(disasters_percentages) * sum([resistance * d_percentage + (1 - d_percentage) for d_percentage, resistance in zip(disasters_percentages, crops[crop_name].resistances)])
        crop_yield = (v["yieldAmount"] + crop_proportion) / (100 + v["proportion"])
        crop_growth = min(v["growth"] / 100 + 0.25, 1)
        
        out[crop_name] = {"yieldAmount": "%.2f" % crop_yield, "proportion": "%.2f" % crop_proportion, "growth": "%.2f" % (crop_growth * 100)}

    return out
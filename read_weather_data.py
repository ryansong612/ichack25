import xarray as xr
import numpy as np

from geopy import geocoders
from geopy.geocoders import Nominatim

def lag_and_lon(location):
    geolocator = Nominatim(user_agent='x@gmail.com')

    result = geolocator.geocode(location, timeout = 100)
    
    return result.latitude, result.longitude

def get_weather_condition(location):
    latitude, longitude = lag_and_lon(location)

    data = ["ta", "pr", "hur", "ua"]

    # Load CMIP6 future projection dataset (replace with actual path)
    filepaths = ["./dataset/ta_Amon_EC-Earth3-Veg_ssp119_r1i1p1f1_gr_20300116-20301216.nc", "./dataset/pr_Amon_EC-Earth3-Veg_ssp119_r1i1p1f1_gr_20300116-20301216.nc", "./dataset/hur_Amon_EC-Earth3-Veg_ssp119_r1i1p1f1_gr_20300116-20301216.nc", "./dataset/ua_Amon_EC-Earth3-Veg_ssp119_r1i1p1f1_gr_20300116-20301216.nc"]

    datasets = []

    for f in filepaths:
        datasets.append(xr.open_dataset(f))

    weather_cond = {}

    for i, prop in enumerate(data):
        ds = datasets[i]
        ds_selected = ds.sel(lat=latitude, lon=longitude, method="nearest")
        
        weather_cond[prop] = [float(value) if isinstance(value, np.float32) else float(value[0]) for value in ds_selected[prop].values]

    return weather_cond

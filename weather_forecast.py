
import requests
from dotenv import load_dotenv
import os
from geopy import geocoders
from geopy.geocoders import Nominatim

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def weather_forecast(location):
    geolocator = Nominatim(user_agent='x@gmail.com')

    result = geolocator.geocode(location, timeout = 100)
    
    return forecast(result.latitude, result.longitude)

def forecast(lat, lon):
    # OpenWeather API Key
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }

    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=params)

    if response.status_code != 200:
        return f"Error: {response.json()}"

    data = response.json()

    # Find weather data for tomorrow
    forecasts = data['list']
    
    if not forecasts:
        return "No forecast data available for tomorrow."

    summary = [
        {
            "date": f['dt_txt'],
            "temperature": f['main']['temp'],
            "pressure": f['main']['pressure'],
            "humidity": f['main']['humidity'],
            "weather": f['weather'][0]['main'],
            "description": f['weather'][0]['description'],
            "wind": {
                "speed_kmh": f['wind']['speed'] * 3.6,  # Convert m/s to km/h
                "direction": f['wind']['deg'],
                "gust": f['wind']['gust']
            },
            "cloud_coverage": f['clouds']['all'],
            "visibility_km": f.get('visibility', 10000) / 1000,  # Convert meters to km
        }
        for f in forecasts
    ]

    return summary

print(weather_forecast("London"))
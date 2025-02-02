import anthropic
from dotenv import load_dotenv
import os

import xml.etree.ElementTree as ET

# Call this function with the weather data to get the event prediction in a dictionary
def weather_to_event(weather_data):
    load_dotenv()
    API_KEY = os.getenv("ANTHROPIC_API_KEY")

    client = anthropic.Anthropic(
        api_key=API_KEY,
    )
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt(weather_data)},
        ]
    )

    return format_response(message.content[0].text)

# This function generates the prompt for the AI
def prompt(weather_dict):
    with open("ai_prompt.txt", "r", encoding="utf-8") as file:

        prompt = file.read()
        print(weather_dict)
        prompt = prompt.replace("{{WEATHER_CONDITIONS}}", str(weather_dict))
        return prompt

def extract_xml_content(text):
    start = text.find("<disaster_analysis>")
    end = text.find("</disaster_analysis>")
    return text[start:end + len("</disaster_analysis>")].strip()

# This function formats the response from the AI (input is the text)
def format_response(response):
    # Remove the introduction and conclusion
    data = extract_xml_content(response)

    print(data)

    root = ET.fromstring(data)
    disasters = {}

    for disaster in root.findall('disaster'):
        name = disaster.find('name').text
        probability = disaster.find('probability').text
        
        parameters = {}
        param_text = disaster.find('parameters').text
        if param_text:
            for line in param_text.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    parameters[key.strip()] = value.strip()
        
        changes = {}
        changes_text = disaster.find('changes').text
        if changes_text:
            for line in changes_text.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    changes[key.strip()] = value.strip()
        
        disasters[name] = {
            "probability": probability,
            "parameters": parameters,
            "changes": changes
        }

    return disasters

# example_data = """ {'date': '2025-02-06 21:00:00', 'temperature': 276.81, 'pressure': 1037, 'humidity': 83, 'weather': 'Clouds', 'description': 'scattered clouds', 'wind': {'speed_kmh': 10.836, 'direction': 47, 'gust': 8.53}, 'cloud_coverage': 27, 'visibility_km': 10.0}"""
# example_response =  """
#     I'll analyze the weather conditions from the example and provide disaster predictions.
#     <disaster_analysis>
#     <disaster>
#     <name>Disease</name>
#     <probability>65%</probability>
#     <parameters>

#     Diffusion coefficient: 0.72
#     Infection probability: 0.65
#     Initial_sickness_value: 0.58
#     </parameters>


#     <changes>
#     temperature: -0.5K
#     pressure: +2
#     humidity: +5
#     weather: "Overcast clouds"
#     description: "overcast clouds"
#     wind_speed: -1.2 km/h
#     cloud_coverage: +15
#     visibility_km: -2.0
#     </changes>
#     </disaster>
#     <disaster>
#     <name>Flooding</name>
#     <probability>15%</probability>
#     <parameters>
#     - Duration: 6 hours
#     </parameters>
#     <changes>
#     temperature: -1.2K
#     pressure: -5
#     humidity: +12
#     weather: "Rain"
#     description: "moderate rain"
#     wind_speed: +2.5 km/h
#     cloud_coverage: +45
#     visibility_km: -4.0
#     </changes>
#     </disaster>
#     <disaster>
#     <name>Drought</name>
#     <probability>5%</probability>
#     <parameters>
#     - Duration: 3 hours
#     </parameters>
#     <changes>
#     temperature: +2.0K
#     pressure: +8
#     humidity: -15
#     weather: "Clear"
#     description: "clear sky"
#     wind_speed: -3.0 km/h
#     cloud_coverage: -20
#     visibility_km: +2.0
#     </changes>
#     </disaster>
#     <disaster>
#     <name>Heatwave</name>
#     <probability>8%</probability>
#     <parameters>
#     - Temperature: 285K
#     </parameters>
#     <changes>
#     temperature: +4.5K
#     pressure: -3
#     humidity: -25
#     weather: "Clear"
#     description: "clear sky"
#     wind_speed: -5.0 km/h
#     cloud_coverage: -15
#     visibility_km: +1.5
#     </changes>
#     </disaster>
#     <disaster>
#     <name>ColdSnap</name>
#     <probability>25%</probability>
#     <parameters>
#     - Temperature: 273K
#     </parameters>
#     <changes>
#     temperature: -3.8K
#     pressure: +6
#     humidity: +8
#     weather: "Clear"
#     description: "clear sky"
#     wind_speed: -2.5 km/h
#     cloud_coverage: -10
#     visibility_km: +3.0
#     </changes>
#     </disaster>
#     <disaster>
#     <name>Wind</name>
#     <probability>12%</probability>
#     <parameters>
#     - Windspeed: 15 knots
#     </parameters>
#     <changes>
#     temperature: -0.8K
#     pressure: -4
#     humidity: -5
#     weather: "Clouds"
#     description: "broken clouds"
#     wind_speed: +12.5 km/h
#     cloud_coverage: +25
#     visibility_km: -1.5
#     </changes>
#     </disaster>
#     </disaster_analysis>
#     This analysis is based on the given weather conditions showing scattered clouds, relatively low temperature (276.81K), high pressure (1037), and high humidity (83%). Disease has the highest probability due to the combination of high humidity and moderate temperatures. ColdSnap is the second most likely due to the already low temperature. Other disasters have lower probabilities given the stable pressure and moderate wind conditions.
    
#     Hello
#     - hi
#     - hi
#     """

# print(weather_to_event(example_data))
# print(format_response(example_response))
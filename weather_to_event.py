import anthropic
from read_weather_data import get_weather_condition
from config import API_KEY

import xml.etree.ElementTree as ET

# Call this function with the weather data to get the event prediction in a dictionary
def weather_to_event(curr_month, location):
    weather_data = get_weather_condition(location)
    
    curr_data = {key: weather_data[key][curr_month - 1] for key in list(weather_data.keys())}
    client = anthropic.Anthropic(
        api_key=API_KEY,
    )
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt(curr_data)},
        ]
    )

    print(message.content[0].text)

    return format_response(message.content[0].text)

# This function generates the prompt for the AI
def prompt(weather_dict):
    with open("ai_prompt.txt", "r", encoding="utf-8") as file:

        prompt = file.read()
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
        
        disasters[name] = {
            "probability": probability,
        }

    return disasters

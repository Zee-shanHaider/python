import requests
from datetime import datetime, timedelta


def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    return response.json()['current']['temperature_2m'], response.json()['current']['interval']

city = {
    "Karachi": (34.01, 71.57),
    "Islamabad": (33.68, 73.04),
    "Lahore": (31.55, 74.35),
    "Multan": (30.15, 71.48),
    "Murree": (33.90, 73.38),
    "Quetta": (30.17, 67.01),
    "Peshawar": (34.01, 71.57),
}

for city_name, (latitude, longitude) in city.items():
    temp, interval = get_weather(latitude, longitude)
    print(f"Weather in {city_name}: {temp}")
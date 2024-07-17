import requests
from weather_app.secrets import API_KEY


def get_weather(city):
    api_key = API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
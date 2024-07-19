import requests
from weather_app.secrets import API_KEY


def get_weather(city):
    api_key = API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': api_key}
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {'error': 'The request timed out. Please try again later.'}
    except requests.exceptions.RequestException as e:
        return {'error': f'An error occurred: {e}'}


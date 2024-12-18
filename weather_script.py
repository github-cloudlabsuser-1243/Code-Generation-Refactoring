import requests

# Function to get weather data from OpenWeatherMap API

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    import os
    api_key = os.getenv("c7c51bb77d9018aa3141d03ab118a940")
    if not api_key:
        raise ValueError("No API key found. Please set the OPENWEATHER_API_KEY environment variable.")
    city = "London"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to retrieve weather data")
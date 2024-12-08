import requests
from typing import Dict, Union


class WeatherAPI:
    """
    A class to interact with the OpenWeatherMAP API and fetch weather data.

    Attributes:
    BASE_URL (str): The base URL for the OpenWeatherAPI.
    api_key (str): API key for authenticating requests.
    """

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        """
        Initializes the WeatherAPI with an API key.

        Args:
            api_key(str): Asher Valentini's OpenWeatherAPI key.
        """
        self.api_key = api_key

    def fetch_weather(self, city):
        """
        Fetches weather data for a given city.

        Args:
            city(str): The name of the city to fetch weather for.

        Returns:
            dict: Weather data with keys 'city', 'temperature', 'description' on success.
            dict: Error data with key 'error' on failure.
        """
        params = {"q": city, "appid": self.api_key, "units": "metric"}

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise HTTPError for 4xx or 5xx responses
        except requests.exceptions.HTTPError as http_err:
            # Return HTTP error code
            return {"error": response.status_code}
        except requests.exceptions.RequestException as req_err:
            # Return string error message for non-HTTP issues
            return {"error": f"Request failed: {str(req_err)}"}

        # Succesful request
        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather = data["weather"][0]
            return {
                "city": city,
                "temperature": main["temp"],
                "description": weather["description"],
            }
        else:
            return {"error": response.status_code}

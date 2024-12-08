import aiohttp
from typing import Dict, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

    async def fetch_weather(
        self, city: str
    ) -> Union[Dict[str, Union[str, int]], Dict[str, str]]:
        """
        Fetches weather data for a given city.

        Args:
            city(str): The name of the city to fetch weather for.

        Returns:
            dict: Weather data with keys 'city', 'temperature', 'description' on success.
            dict: Error data with key 'error' on failure.
        """
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.BASE_URL, params=params) as response:
                    response.raise_for_status()  # Raise HTTPError for 4xx or 5xx responses
                    # Succesful request
                    if response.status == 200:
                        data = await response.json()
                        main = data["main"]
                        weather = data["weather"][0]
                        logger.info(f"Successfull fetched weather for {city}")
                        return {
                            "city": city,
                            "temperature": main["temp"],
                            "description": weather["description"],
                        }
                    else:
                        return {"error": response.status}
            except aiohttp.ClientResponseError as http_err:
                # Return HTTP error code
                logger.info(f"API request failed: {http_err}")
                return {"error": http_err.status}
            except aiohttp.ClientError as req_err:
                # Return string error message for non-HTTP issues
                logger.info("API request failed: {req_err}")
                return {"error": f"Request failed: {str(req_err)}"}

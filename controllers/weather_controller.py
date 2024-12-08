import logging
from models.api_model import WeatherAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WeatherController:
    """
    The controller class that bridges the view and the weatherAPI modules.

    Attributes:
        api (WeatherAPI): The WeatherAPI instance for fetching weather data.
    """

    def __init__(self):
        """
        Initializes the WeatherController with the WeatherAPI instance.
        """
        self.api = WeatherAPI("de4dfcfd5ab05531b01c5bcd9c923e3c")

    async def get_weather(self, city: str):
        """
        Fetches weather data for a given city via the WeatherAPI.

        Args:
            city(str): the city to fetch weather data for.

        Returns:
            dict: Weather data or error data.
        """
        logger.info(f"Fetching weather for {city}")
        return await self.api.fetch_weather(city)

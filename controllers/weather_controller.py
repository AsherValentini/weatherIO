from models.api_model import WeatherAPI


class WeatherController:
    def __init__(self):
        self.api = WeatherAPI("de4dfcfd5ab05531b01c5bcd9c923e3c")

    def get_weather(self, city):
        return self.api.fetch_weather(city)

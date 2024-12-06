import requests


class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather = data["weather"][0]
            return response.status_code, {
                "city": city,
                "temperature": main["temp"],
                "description": weather["description"],
            }
        else:
            return {"error": response.status_code}

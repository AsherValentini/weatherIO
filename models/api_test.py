import requests

API_KEY = "de4dfcfd5ab05531b01c5bcd9c923e3c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(BASE_URL, params=params)

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


if __name__ == "__main__":
    status_code, data = fetch_weather("London")
    print(f"Status Code : {status_code}")
    print(f"Data: {data}")

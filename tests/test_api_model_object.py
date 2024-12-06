from models.api_model import WeatherAPI


def test_weather_api_valid_city():
    api = WeatherAPI("de4dfcfd5ab05531b01c5bcd9c923e3c")
    status_code, result = api.fetch_weather("London")
    assert "temperature" in result
    assert "description" in result
    assert result["city"] == "London"


def test_weather_api_invalid_city():
    api = WeatherAPI("de4dfcfd5ab05531b01c5bcd9c923e3c")
    result = api.fetch_weather("zebra ville")
    assert "error" in result
    assert result["error"] == 404

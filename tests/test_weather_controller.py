from controllers.weather_controller import WeatherController

import pytest


@pytest.fixture
def controller():
    return WeatherController()


def test_controller_fetch_valid_city(controller):
    result = controller.get_weather("London")
    assert "city" in result
    assert "temperature" in result
    assert "description" in result
    assert result["city"] == "London"


def test_controller_fetch_invalid_city(controller):
    result = controller.get_weather("invalid city")
    assert "error" in result

from controllers.weather_controller import WeatherController

import pytest


@pytest.fixture
def controller():
    return WeatherController()


@pytest.mark.asyncio
async def test_controller_fetch_valid_city(controller):
    result = await controller.get_weather("London")
    assert "city" in result
    assert "temperature" in result
    assert "description" in result
    assert result["city"] == "London"


@pytest.mark.asyncio
async def test_controller_fetch_invalid_city(controller):
    result = await controller.get_weather("invalid city")
    assert "error" in result
    assert isinstance(result["error"], (int, str))

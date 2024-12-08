import pytest
from models.api_model import WeatherAPI


@pytest.fixture
def api():
    return WeatherAPI("de4dfcfd5ab05531b01c5bcd9c923e3c")


@pytest.mark.asyncio
async def test_fetch_weather_valid_city(api):
    result = await api.fetch_weather("London")
    assert "city" in result
    assert "temperature" in result
    assert "description" in result
    assert result["city"] == "London"


@pytest.mark.asyncio
async def test_fetch_weather_invalid_city(api):
    result = await api.fetch_weather("invalid city")
    assert "error" in result
    assert isinstance(result["error"], (int, str))

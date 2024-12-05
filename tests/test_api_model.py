import pytest

from models.api_test import fetch_weather


def test_fetch_weather_valid_city():
    status_code, result = fetch_weather("London")
    assert status_code == 200
    assert "temperature" in result
    assert "description" in result
    assert result["city"] == "London"


def test_fetch_weather_invalid_city():
    result = fetch_weather("InvalidCityName")
    assert "error" in result
    assert result["error"] == 404

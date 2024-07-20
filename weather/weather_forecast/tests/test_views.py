from django.test import TestCase, Client
from django.urls import reverse
from weather_forecast.models import City, CitySearchQuery
from unittest.mock import patch


class WeatherForecastViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        City.objects.create(country="TestCountry", city="TestCity")

    @patch("weather_forecast.service.forecast_service.WeatherApiService.get_weather")
    def test_get_weather_forecast(self, mock_get_weather):
        mock_get_weather.return_value = {
            "location": {"name": "TestCity"},
            "current": {"temp_c": 20},
        }
        response = self.client.post(reverse("weather_forecast"), {"city": "TestCity"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather_forecast/weather_forecast_post.html")
        self.assertContains(response, "TestCity")
        self.assertContains(response, "20")

    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather_forecast/index.html")


class CityAutocompleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        City.objects.create(country="TestCountry", city="TestCity")

    def test_city_autocomplete(self):
        response = self.client.get(reverse("city_autocomplete"), {"q": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, ["TestCity"])

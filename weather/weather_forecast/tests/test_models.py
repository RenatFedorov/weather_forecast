from django.test import TestCase
from weather_forecast.models import City, CitySearchQuery


class CityModelTest(TestCase):
    def setUp(self):
        City.objects.create(country="TestCountry", city="TestCity")

    def test_city_creation(self):
        city = City.objects.get(city="TestCity")
        self.assertEqual(city.country, "TestCountry")
        self.assertEqual(city.city, "TestCity")
        self.assertEqual(str(city), "TestCountry, TestCity")


class CitySearchQueryModelTest(TestCase):
    def setUp(self):
        CitySearchQuery.objects.create(session_key="testsessionkey", city="TestCity")

    def test_city_search_query_creation(self):
        search_query = CitySearchQuery.objects.get(city="TestCity")
        self.assertEqual(search_query.session_key, "testsessionkey")
        self.assertEqual(search_query.city, "TestCity")
        self.assertTrue(search_query.date is not None)
        self.assertEqual(str(search_query), "TestCity")

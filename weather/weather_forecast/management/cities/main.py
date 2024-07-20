from weather_forecast.management.cities.extract import ApiDataLoader
from weather_forecast.management.cities.service import CityDataFacade
from weather_forecast.management.cities.load import CitySaver
import time


def create_cities():
    url = "https://countriesnow.space/api/v0.1/countries"
    data_loader = ApiDataLoader(url)
    city_saver = CitySaver()
    city_data_facade = CityDataFacade(data_loader, city_saver)
    city_data_facade.load_and_save_cities()


try:
    create_cities()
except Exception as e:
    print(f"Error initializing cities: {e}")

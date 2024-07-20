from weather_forecast.cities.extract import ApiDataLoader
from weather_forecast.cities.service import CityDataFacade
from weather_forecast.cities.load import CitySaver
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

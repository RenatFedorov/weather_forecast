from weather_forecast.cities.abstract_class import DataLoader
from weather_forecast.cities.load import CitySaver


class CityDataFacade:
    def __init__(self, data_loader: DataLoader, city_saver: CitySaver):
        """
        Initialize the CityDataFacade with a data loader and city saver.

        :param data_loader: An instance of DataLoader to load data.
        :param city_saver: An instance of CitySaver to save data.
        """
        self.data_loader = data_loader
        self.city_saver = city_saver

    def load_and_save_cities(self) -> None:
        """
        Load data using the data loader and save it using the city saver.
        """
        data = self.data_loader.load_data()
        self.city_saver.save_cities(data)

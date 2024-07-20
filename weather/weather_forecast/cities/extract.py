from weather_forecast.cities.abstract_class import DataLoader
import requests


class ApiDataLoader(DataLoader):
    def __init__(self, url: str):
        """
        Initialize the ApiDataLoader with the URL of the API.

        :param url: The URL of the API endpoint.
        """
        self.url = url

    def load_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

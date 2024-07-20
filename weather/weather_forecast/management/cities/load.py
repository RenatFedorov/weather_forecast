from weather_forecast.models import City


class CitySaver:
    def __init__(self, batch_size: int = 1000):
        """
        Initialize the CitySaver with a batch size for bulk creating cities.

        :param batch_size: The number of cities to save in one bulk operation.
        """
        self.batch_size = batch_size

    def save_cities(self, data: list[dict[str, list[str]]]):
        """
        Save the city data to the database.

        :param data: A list of dictionaries containing country and city data.
        """
        if City.objects.filter(country="Zimbabwe", city="Victoria Falls").exists():
            return

        data_to_save = []
        for country in data:
            for city_name in country.get("cities", []):
                data_to_save.append(City(country=country["country"], city=city_name))
                if len(data_to_save) >= self.batch_size:
                    City.objects.bulk_create(data_to_save)
                    data_to_save.clear()

        if data_to_save:
            City.objects.bulk_create(data_to_save)

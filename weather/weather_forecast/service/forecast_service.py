from weather_forecast.models import City, CitySearchQuery
import requests
from django.conf import settings


class CityService:
    """
    Service class for city-related operations.
    """

    @staticmethod
    def get_city_suggestions(query: str) -> list:
        """
        Get city suggestions based on the query.

        :param query: The search query to find city suggestions.
        :type query: str
        :return: A list of up to 10 city names starting with the query string.
        :rtype: list
        """
        suggestions = (
            City.objects.filter(city__istartswith=query)
            .values_list("city", flat=True)
            .distinct()[:10]
        )
        return list(suggestions)


class WeatherApiService:
    """
    Service class for weather-related operations.
    """

    api_key = settings.FORECAST_API_KEY

    def get_weather(self, city: str) -> dict:
        """
        Get weather forecast for the given city.

        :param city: The name of the city for which to get the weather forecast.
        :type city: str
        :return: A dictionary containing the weather forecast for the given city.
        :rtype: dict
        """
        response = requests.get(
            f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days=3"
        )
        return response.json()


class SearchHistoryService:
    """
    Service class for search history operations.
    """

    @staticmethod
    def save_search_query(session_key: str, city: str) -> None:
        """
        Save the city search query.

        :param session_key: The session key of the user.
        :type session_key: str
        :param city: The name of the city searched by the user.
        :type city: str
        :return: None
        """
        CitySearchQuery.objects.create(
            city=city.title().strip(),
            session_key=session_key,
        )

    @staticmethod
    def get_last_city(session_key: str) -> CitySearchQuery:
        """
        Get the last searched city for the given session.

        :param session_key: The session key of the user.
        :type session_key: str
        :return: The last searched city for the given session, or None if no search history exists.
        :rtype: CitySearchQuery
        """
        return (
            CitySearchQuery.objects.filter(session_key=session_key)
            .values_list("city", flat=True)
            .order_by("-date")
            .first()
        )

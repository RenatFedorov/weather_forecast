from django.db.models import Count
from rest_framework import generics
from weather_forecast.api.v1.serializers import CitySearchSerializer
from weather_forecast.api.v1.pagination import CitySearchPagination
from weather_forecast.models import CitySearchQuery


class CitySearchListView(generics.ListAPIView):
    """
    API view to list city search queries with pagination.
    """
    serializer_class = CitySearchSerializer
    pagination_class = CitySearchPagination

    def get_queryset(self):
        """
        Retrieves the queryset of city search queries for the current session.

        :return: The filtered and annotated queryset or an empty queryset.
        :rtype: QuerySet
        """
        if session_key := self.request.session.session_key:
            return (
                CitySearchQuery.objects.filter(session_key=session_key)
                .values("city")
                .annotate(search_count=Count("city"))
                .order_by("-search_count")
            )
        return CitySearchQuery.objects.none()

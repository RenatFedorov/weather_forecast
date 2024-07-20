from rest_framework import serializers

from weather_forecast.models import CitySearchQuery


class CitySearchSerializer(serializers.ModelSerializer):
    """
    Serializer for city search queries with search count.
    """
    search_count = serializers.IntegerField()

    class Meta:
        model = CitySearchQuery
        fields = ["city", "search_count"]

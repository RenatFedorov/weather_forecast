from django.db import models


class City(models.Model):
    """
    Model representing a city and its country.
    """

    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.country}, {self.city}"


class CitySearchQuery(models.Model):
    """
    Model representing a search query for a city.
    """

    session_key = models.CharField(max_length=40, null=False, default="asdasd")
    city = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}"

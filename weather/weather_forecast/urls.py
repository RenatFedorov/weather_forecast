from django.urls import include, path
from weather_forecast import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forecast/", views.get_weather_forecast, name="weather_forecast"),
    path("autocomplete/", views.city_autocomplete, name="city_autocomplete"),
    path("api/v1/", include("weather_forecast.api.v1.urls")),
]

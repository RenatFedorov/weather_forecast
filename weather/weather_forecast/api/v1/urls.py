from django.urls import path
from weather_forecast.api.v1 import views

urlpatterns = [
    path("city_searches/", views.CitySearchListView.as_view(), name="city_searches"),
]

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from weather_forecast.service.forecast_service import (
    CityService,
    WeatherApiService,
    SearchHistoryService,
)


def index(request):
    """
    Render the index page with the last searched city.
    """
    last_city: str = SearchHistoryService.get_last_city(request.session.session_key)
    return render(request, "weather_forecast/index.html", {"last_city": last_city})


def get_weather_forecast(request):
    """
    Handle the weather forecast request.
    """
    if not request.session.session_key:
        request.session.save()
    if request.method == "POST":
        if city := request.POST.get("city"):
            print(request.session.session_key)
            SearchHistoryService.save_search_query(request.session.session_key, city)
            weather_data: dict = WeatherApiService().get_weather(city)
            return render(
                request,
                "weather_forecast/weather_forecast_post.html",
                {"weather": weather_data},
            )
    return HttpResponseRedirect(reverse("index"))


def city_autocomplete(request):
    """
    Handle city autocomplete requests.
    """
    query: str = request.GET.get("q", "")
    suggestions: list = CityService.get_city_suggestions(query)
    return JsonResponse(suggestions, safe=False)

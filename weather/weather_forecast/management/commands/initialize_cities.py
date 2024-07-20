from django.core.management.base import BaseCommand
from weather_forecast.management.cities.main import create_cities


class Command(BaseCommand):
    help = "Initialize cities data"

    def handle(self, *args, **kwargs):
        create_cities()
        self.stdout.write(self.style.SUCCESS("Successfully initialized cities data"))

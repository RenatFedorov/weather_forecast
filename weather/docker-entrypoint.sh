#!/usr/bin/env bash

sleep 10
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py initialize_cities

gunicorn weather.wsgi:application --bind 0.0.0.0:8000 --workers 1
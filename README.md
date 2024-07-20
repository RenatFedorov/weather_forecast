# Weather Forecast Application

## Описание проекта

Этот проект представляет собой веб-приложение для прогноза погоды. Оно позволяет пользователям искать погоду в городах, сохранять историю поиска и просматривать последний искомый город. Проект использует Django для создания API и PostgreSQL для хранения данных.

## Стек технологий

- Python 3.10
- Django
- Django rest framework
- gunicorn
- requests
- PostgreSQL
- Docker
- Nginx

## Установка

### Шаги для установки

1. Склонируйте репозиторий:
    ```sh
    git clone git@github.com:RenatFedorov/weather_forecast.git
    cd weather_forecast
    ```

2. Создайте `.env` файлы для конфигурации окружения в директориях `weather` и `db`.

3. Запустите Docker Compose:
    ```sh
    docker-compose up --build
    ```

## Использование

После запуска контейнеров, приложение будет доступно по адресу http://0.0.0.0/weather/.


##  API
Получение информации о количестве запросов по городам

    URL: /weather/api/v1/city_searches/
    Метод: GET
    Описание: Возвращает информацию о том, сколько раз пользователь вводил города.   

## Команда
Инициализация городов в базе данных

    Команда: python3 manage.py initialize_cities
    Описание: Создает записи для всех городов в базе данных. В дальнейшем города используются для автодополнения в поиске.

## Что было реализовано   

1. Написаны тесты
2. Приложение помещено в Docker контейнер
3. Автодополнение при вводе города
4. Если пользователь уже искал погоду на сайте, то будет предложено снова искать погоду, в последней городе поиска
5. В БД сохраняется история поиска пользователей
6. API для пользователя, показывающее какие города он искал и сколько раз выполнялся поиск для конкретного города

FROM python:3.10

ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN  pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY ./weather/ .

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
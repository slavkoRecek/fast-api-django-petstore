#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


if [ "$SERVICE" = "api" ]; then
  python manage.py migrate --noinput
#  gunicorn foodie.wsgi:application --config=gunicorn.conf.py
  uvicorn application.asgi:app --host 0.0.0.0 --port 8000
else
  exec "$@"
fi

#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

echo "PostgreSQL started"

# python manage.py collectstatic --no-input --clear
python manage.py makemigrations --no-input
python manage.py migrate --no-input

exec "$@"
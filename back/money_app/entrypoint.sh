#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

echo "PostgreSQL started"

# uv /home/src/manage.py collectstatic --no-input --clear
uv run /home/src/manage.py makemigrations --no-input
uv run /home/src/manage.py migrate --no-input

exec "$@"
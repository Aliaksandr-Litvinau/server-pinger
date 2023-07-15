#!/bin/bash

# Here we can do healthchecks and other management commands

set -o errexit # fails if it encounters an error

ls -la

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"

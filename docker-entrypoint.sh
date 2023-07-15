#!/bin/bash

# Here we can do healthchecks and other management commands

set -o errexit # fails if it encounters an error

ls -la

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py makemigrations
python manage.py migrate

exec "$@"

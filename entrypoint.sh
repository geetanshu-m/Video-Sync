#!/bin/bash

pipenv run python manage.py migrate --noinput

pipenv run gunicorn VideoSync.wsgi:application -w 1 --threads 12 --reload --bind 0.0.0.0:8080

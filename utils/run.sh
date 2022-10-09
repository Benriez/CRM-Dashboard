#!/bin/sh
python manage.py collectstatic --noinput && python manage.py migrate && gunicorn django_backend.wsgi --bind=0.0.0.0:80


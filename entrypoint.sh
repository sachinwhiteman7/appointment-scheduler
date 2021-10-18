#!/bin/bash

#create migration files
echo "make migrations >>>>>>>>>"
python manage.py makemigrations

#migrate database
echo "migrate >>>>>>>>>"
python manage.py migrate

#create static file folder
echo "collectstatic >>>>>>>>>"
python manage.py collectstatic --no-input

# Start server
echo "bff Starting server"
python manage.py runserver 0.0.0.0:8000
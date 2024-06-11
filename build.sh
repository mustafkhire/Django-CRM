#!/bin/bash

#Build dcrm project
echo " Building the project..."
python3.8.0 -m pip install -r requirements.txt

echo " Make Migration..."
python3.8.0 manage.py makemigrations --noinput
python3.8.0 manage.py migrate --noinput

echo "Collect Static..."
python3.8.0 manage.py collectstatic --noinput --clear
#!/bin/bash

python -mpip list --format json > pip-info.json
python manage.py migrate

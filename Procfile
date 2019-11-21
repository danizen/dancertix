web: gunicorn --access-logfile - -w 3 --threads 5 conf.wsgi --preload
release: python manage.py migrate

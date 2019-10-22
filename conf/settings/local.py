from rds_secrets.django import SecretsManagerDBConfig
from .base import *

# Debug Toolbar needs these
INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_DB_SECRET', 'django-test-dancertix-app')

DATABASES = {
    'default': SecretsManagerDBConfig(secret_id=__secret_id, HOST='localhost', PORT=5432)
}


# The next two overrides presume you're using manage.py runserver, which uses HTTP.
# On the servers, HTTPS is required.

CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False

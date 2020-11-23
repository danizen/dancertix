from .base import *

# Debug Toolbar needs these
INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_DB_SECRET', 'django-test-dancertix-app')
__port = int(os.environ.setdefault('DJANGO_DB_PORT', '5432'))

DATABASES = {
    'default': {
        'ENGINE': 'rds_secrets.backends.postgresql',
        'SECRET': __secret_id,
        'HOST': 'localhost',
        'PORT': __port,
    }
}

# The next two overrides presume you're using manage.py runserver, which uses HTTP.
# On the servers, HTTPS is required.

CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False

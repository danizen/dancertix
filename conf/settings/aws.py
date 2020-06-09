from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_DB_SECRET', 'django-test-dancertix-app')

STATIC_URL = 'https://assets.nlm.nih.gov/dancertix/dev/'

DATABASES = {
    'default': {
        'ENGINE': 'rds_secrets.django.backends.postgresql',
        'SECRET': __secret_id,
    }
}

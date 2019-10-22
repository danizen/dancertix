from rds_secrets.django import SecretsManagerDBConfig
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_SECRET', 'django-test-dancertix-app')

DATABASES = {
    'default': SecretsManagerDBConfig(secret_id=__secret_id)
}


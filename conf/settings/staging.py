from .base import *
from rds_secrets.django import SecretsManagerDBConfig

# Debug Toolbar needs these
INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ('127.0.0.1', '130.14.160.*')

DEBUG = True

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_SECRET', 'NLM-INT-dancertix-app')
DATABASES = {
    'default': SecretsManagerDBConfig(secret_id=__secret_id)
}

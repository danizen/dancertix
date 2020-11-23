from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Modify the following sections to use the appropriate secret name.
__secret_id = os.environ.setdefault('DJANGO_DB_SECRET', 'django-test-dancertix-app')

STATIC_URL = 'https://assets.nlm.nih.gov/dancertix/dev/'

# Staticfiles should use Django storages
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'nlm-sbox-ab-django-app-django-test-us-east-1'
AWS_DEFAULT_ACL = 'public-read'

# TODO: Fix the settings below
CLOUDFRONT_DOMAIN = "your cloudfront domain"
CLOUDFRONT_ID = "your cloud front id"
AWS_S3_CUSTOM_DOMAIN = "same as your cloud front domain"

# Why are both required?
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

DATABASES = {
    'default': {
        'ENGINE': 'rds_secrets.backends.postgresql',
        'SECRET': __secret_id,
    }
}


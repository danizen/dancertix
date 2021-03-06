"""
Django settings for dancertix project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# This file contains only the settings that will remain the same through
# the software development cycle. Settings that change from stage to
# stage in development are pulled out into dev_sqlite3.py, dev_oracle.py,
# integration.py, aws.py, and aws.py. Each of those files will import
# this one.

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('SECRET_KEY', 'z3_r&d8dv)-q)fv(6pu*^_#3&ezh((!%xi*5x6#1x4=y!#2_89')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party external apps
    'crispy_forms',
    'bootstrap_pagination',
    'social_django',
    'django_filters',
    'rest_framework',

    # third party internal apps
    'cloudauth',
    'cloudauth_admin',
    'rds_secrets',

    'dancertix',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cloudauth.context_processors.sanitized_request',
                'cloudauth.context_processors.remote_may_login',
                'cloudauth.context_processors.user_group_names',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Database information is not specified here; look in the
# file settings/dev_sqlite3.py etc. for the settings relevant
# to each stage of development.

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# There are three settings associated with paths and static files:
#
#      STATIC_URL ......... This tells Django how to render a url for static files.
#      STATICFILES_DIRS ... This tells Django where to look for static files,
#                           beyond application static directories, when DEBUG=True.
#      STATIC_ROOT ........ This names the directory into which "manage.py collectstatic"
#                           will gather the static files when it's time to move to the
#                           integration server.

STATIC_URL = '/public/'
STATIC_ROOT = os.path.join(BASE_DIR, "public")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'vendor'),
]


CRISPY_FAIL_SILENTLY = True

# Let the crispy-forms package know that it should use Bootstrap4 markup.
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Tell the 'assets_static' template tag
ASSETS_STATIC_REMOTE_PREFIX = 'https://assets.nlm.nih.gov/assets/'

# Auth/Auth settings

LOGIN_ERROR_URL = '/error/'
LOGIN_REDIRECT_URL = '/'

__domain = os.environ.setdefault('COGNITO_DOMAIN', 'login.awsint.nlm.nih.gov')

SOCIAL_AUTH_POOL_DOMAIN = 'https://' + __domain
SOCIAL_AUTH_WHITELISTED_REMOTES = ('130.14', '2607:f220:41e', '2607:f220:411')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'cloudauth.pipeline.add_remote_ipaddr',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'cloudauth.pipeline.nihuser_by_username',
    'cloudauth_admin.pipeline.create_external_user',
    'cloudauth_admin.pipeline.verify_internal_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = (
    'cloudauth.backends.CognitoNIH',
)

ADMIN_GROUP = 'Administrators'

CSRF_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True

# Add SESSION_ENGINE....

# Logging

LOGGING_CONFIG = 'occs_core.logging.configure_logging'
LOGGING = {
    'extra_loggers': ['infrastructure', 'dancertix']
}

# For debugging rds_secrets
if os.environ.get('DEBUG_RDS_SECRETS', 'no').lower() in {'1', 'true', 'yes'}:
    BOTO_KWARGS = {
        'region_name': 'us-east-1'
    }
    RDS_CACHE_TIMEOUT = 15.0
    LOGGING['extra_loggers']['rds_secrets'] = {
        'handlers': ['file', 'console'],
        'level': 'DEBUG',
        'propagate': True,
    }

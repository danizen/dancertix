from .heroku import *

# Debug Toolbar needs these
INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False

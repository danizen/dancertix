"""Project werfel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path, include
from django.conf import settings

from django.urls import reverse_lazy

from dancertix.views import *

if 'cloudauth' in settings.INSTALLED_APPS:
    urlpatterns = [
        path('accounts/', include('cloudauth.urls')),
        path('accounts/', include('cloudauth_admin.pipeline_urls')),
        path('internalonly/users/', include('cloudauth_admin.admin_urls')),
        path('infrastructure/', include('infrastructure.urls')),
        path('social/', include('social_django.urls', namespace='social')),
        path('', HomeCBV.as_view(), name='home'),
        path('colors/', ColorsCBV.as_view(), name='colors'),
        path('favorite/', FavoriteColorCBV.as_view(), name='favorite'),
    ]
else:
    urlpatterns = [
        path('accounts/', include('authauth.urls', namespace='cloudauth')),
        path('infrastructure/', include('infrastructure.urls')),
        path('social/', include('social_django.urls', namespace='social')),
        path('', HomeCBV.as_view(), name='home'),
        path('colors/', ColorsCBV.as_view(), name='colors'),
        path('favorite/', FavoriteColorCBV.as_view(), name='favorite'),
    ]

# URLs only for debugging
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

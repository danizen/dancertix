from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
import logging

from occs_core.utils import check_remote_may_login

LOGGER = logging.getLogger(__name__)


class HealthCheckPingView(View):
    def get(self, request):
        return HttpResponse('Status: OK')


class HealthCheckDatabaseView(View):
    def get(self, request):
        try:
            get_user_model().objects.count()
        except:
            response = HttpResponse('Status: cannot reach database')
            response.status_code = 503
            return response
        return HttpResponse('Status: OK')


class CleanPartialsView(View):
    def get(self, request, *args, **kwargs):
        try:
            call_command('cleanpartials')
        except:
            LOGGER.exception('cleanpartials')
            response = HttpResponse( 'Status: clearpartials management command failed' )
            response.status_code = 503
            return response


class CleanSessionsView( View ):
    def get( self, request, *args, **kwargs ):
        if settings.CHECK_ADMIN_IPS and not check_remote_may_login(request):
            return HttpResponseRedirect('/')

        try:
            call_command('clearsessions')
        except:
            LOGGER.exception('clearsessions')
            response = HttpResponse('Status: clearsessions management command failed')
            response.status_code = 503
            return response

        try:
            call_command('django_cas_ng_clean_sessions')
        except:
            LOGGER.exception('clearsessions')
            response = HttpResponse('Status: django_cas_ng_clean_sessions management command failed')
            response.status_code = 503
            return response
        LOGGER.info('clean-sessions success')
        return HttpResponse('Status: OK')

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
import logging

from occs_core.utils import check_remote_may_login

LOG = logging.getLogger(__name__)


class HealthCheckPingView(View):
    def get(self, request):
        LOG.info('health check ping')
        return HttpResponse('Status: OK')


class HealthCheckDatabaseView(View):
    def get(self, request):
        LOG.info('health check db ping')
        try:
            get_user_model().objects.count()
        except:
            response = HttpResponse('Status: cannot reach database')
            response.status_code = 503
            return response
        return HttpResponse('Status: OK')


class CleanSessionsView(View):
    def get(self, request, *args, **kwargs):
        if settings.CHECK_ADMIN_IPS and not check_remote_may_login(request):
            return HttpResponseRedirect('/')

        try:
            LOG.info('cron clearsessions')
            call_command('clearsessions')
        except:
            LOG.exception('clearsessions')
            response = HttpResponse('Status: clearsessions management command failed')
            response.status_code = 503
            return response

        if 'cloudauth' in settings.INSTALLED_APPS:
            try:
                LOG.info('cron cleanpartials')
                call_command('cleanpartials')
            except:
                LOG.exception('cleanpartials')
                response = HttpResponse('Status: clearpartials management command failed')
                response.status_code = 503
                return response

        if 'django_cas_ng' in settings.INSTALLED_APPS:
            try:
                LOG.info('cron django_cas_ng_clean_sessions')
                call_command('django_cas_ng_clean_sessions')
            except:
                LOG.exception('clearsessions')
                response = HttpResponse('Status: django_cas_ng_clean_sessions management command failed')
                response.status_code = 503
                return response

        LOG.info('cron success')
        return HttpResponse('Status: OK')

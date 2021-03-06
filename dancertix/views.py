import json
import logging
import os
import subprocess
from django.utils import timezone
from django.views.generic import FormView, TemplateView
from django.views.generic.list import ListView

from .models import Performance, Dancer, Reservation
from .forms import ColorForm, color_names

__all__ = (
    'HomeCBV',
    'ColorsCBV',
    'FavoriteColorCBV',
    'DeployInfoCBV',
)

LOG = logging.getLogger(__name__)


class ColorsCBV(TemplateView):
    """
    This is a simple view that doesn't use the database at all
    """
    template_name = 'dancertix/colors.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'color_names': color_names
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        LOG.info('colors get')
        return super().get(request, *args, **kwargs)


class HomeCBV(TemplateView):
    """
    The home view reads some data out of the database, but doesn't require login or settings
    """
    template_name = 'dancertix/index.html'
    model = Performance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'performance_list': self.get_performances(),
            'dancer_list': self.get_dancers(),
            'reservation_list': self.get_reservations()
        })
        return context

    def get_performances(self):
        return Performance.objects.filter(start_time__gt=timezone.now()).order_by('title', 'start_time')

    def get_dancers(self):
        return Dancer.objects.only('display_name').order_by('display_name')

    def get_reservations(self):
        if self.request.user.is_authenticated:
            queryset = Reservation.objects.filter(owner=self.request.user)
        else:
            queryset = Reservation.objects.none()
        return queryset

    def get(self, request, *args, **kwargs):
        LOG.info('home get')
        return super().get(request, *args, **kwargs)


class FavoriteColorCBV(FormView):
    template_name = 'dancertix/favorite.html'
    form_class = ColorForm

    def get_success_url(self):
        return self.request.path

    def get_form_kwargs(self):
        initial_color = self.request.session.get('color', '')
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'color': initial_color
        }
        return kwargs

    def form_valid(self, form):
        self.request.session['color'] = form.cleaned_data['color']
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        LOG.info('favorite get')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        LOG.info('favorite post')
        return super().post(request, *args, **kwargs)


class DeployInfoCBV(TemplateView):
    template_name = 'dancertix/deploy.html'

    def get_pip_info(self):
        try:
            info_bytes = subprocess.check_output(['pip','list', '--format', 'json'])
            pipinfo = json.loads(info_bytes)
        except subprocess.CalledProcessError:
            pipinfo = []
        return pipinfo

    def get_context_data(self, **kwargs):
        kwargs.update({
            'info': {
                'pip': self.get_pip_info,
                'headers': dict((k, v) for k, v in self.request.META.items() if k.startswith('HTTP'))
            }
        })
        return super().get_context_data(**kwargs)

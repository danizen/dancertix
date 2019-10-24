from django.utils import timezone
from django.views.generic import FormView, TemplateView
from django.views.generic.list import ListView

from .models import Performance
from .forms import ColorForm, color_names

__all__ = (
    'HomeCBV',
    'ColorsCBV',
    'FavoriteColorCBV'
)


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


class HomeCBV(ListView):
    """
    The home view reads some data out of the database, but doesn't require login or settings
    """
    template_name = 'dancertix/index.html'
    model = Performance

    def get_queryset(self):
        return Performance.objects.filter(start_time__gt=timezone.now()).order_by('title', 'start_time')


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

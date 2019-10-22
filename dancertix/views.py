from django.utils import timezone
from django.views.generic.list import ListView

from .models import Performance

__all__ = (
    'HomeView',
)


class HomeView(ListView):
    template_name = 'dancertix/index.html'
    model = Performance

    def get_queryset(self):
        return Performance.objects.filter(start_time__gt=timezone.now()).order_by('title', 'start_time')

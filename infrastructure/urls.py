from django.urls import path

from .views import (
    CleanSessionsView,
    HealthCheckDatabaseView,
    HealthCheckPingView,
)

app_name = 'infrastructure'
namespace = 'infrastructure'

urlpatterns = [
    path('ping', HealthCheckPingView.as_view(), name='health-check-ping'),
    path('pingdb', HealthCheckDatabaseView.as_view(), name='health-check'),
    path('cron', CleanSessionsView.as_view(), name='cron'),
]

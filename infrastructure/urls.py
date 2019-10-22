from django.urls import path

from .views import (
    CleanPartialsView,
    CleanSessionsView,
    HealthCheckDatabaseView,
    HealthCheckPingView,
)

app_name = 'infrastructure'
namespace = 'infrastructure'

urlpatterns = [
    path(r'^health-check-ping$', HealthCheckPingView.as_view(), name='health-check-ping'),
    path(r'^health-check-db$', HealthCheckDatabaseView.as_view(), name='health-check'),

    # Session tables cleanup:
    path(r'^clean-sessions$', CleanSessionsView.as_view(), name='clean-sessions'),

    # Parctial cleanup
    path(r'^clean-partials$', CleanPartialsView.as_view(), name='clean-partials')
]

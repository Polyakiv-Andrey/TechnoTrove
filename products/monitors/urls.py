from django.urls import path

from products.monitors.views import (
    MonitorListAPIVIew,
    MonitorRetrivAPIView,
    MonitorUltraWideAPIView,
    MonitorGamingAPIView,
    Monitor4KAPIView
)

app_name = "monitors"

urlpatterns = [
    path("", MonitorListAPIVIew.as_view(), name="monitor-list"),
    path("<int:pk>/", MonitorRetrivAPIView.as_view(), name="monitor-ditail"),
    path("geming/", MonitorGamingAPIView.as_view(), name="monitor-gaming"),
    path("4k/", Monitor4KAPIView.as_view(), name="monitor-4k"),
    path("ultra-wide/", MonitorUltraWideAPIView.as_view(), name="monitor-ultra-wide")
]

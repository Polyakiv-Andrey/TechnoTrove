from django.urls import path

from products.monitors.views import MonitorListAPIVIew, MonitorRetrivAPIView

app_name = "monitors"

urlpatterns = [
    path("", MonitorListAPIVIew.as_view(), name="monitor-list"),
    path("<int:pk>/", MonitorRetrivAPIView.as_view(), name="monitor-ditail")
]
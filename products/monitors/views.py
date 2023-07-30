from rest_framework import generics

from products.monitors.models import Monitor
from products.monitors.serializers import MonitorListSerializer, MonitorRetrivSerializer


class MonitorListAPIVIew(generics.ListAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorListSerializer


class MonitorRetrivAPIView(generics.RetrieveAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorRetrivSerializer
    lookup_field = "pk"


class MonitorGamingAPIView(generics.ListAPIView):
    queryset = Monitor.objects.filter(monitor_type=Monitor.MonitorType.gaming)
    serializer_class = MonitorListSerializer


class Monitor4KAPIView(generics.ListAPIView):
    queryset = Monitor.objects.filter(monitor_type=Monitor.MonitorType.fore_k)
    serializer_class = MonitorListSerializer


class MonitorUltraWideAPIView(generics.ListAPIView):
    queryset = Monitor.objects.filter(monitor_type=Monitor.MonitorType.ultra_wide)
    serializer_class = MonitorListSerializer


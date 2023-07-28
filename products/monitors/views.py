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


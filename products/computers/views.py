from rest_framework import generics

from products.computers.models import Computer
from products.computers.serializers import ComputerListSerializer, ComputerRetrivSerializer


class ComputerListAPIVIew(generics.ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerListSerializer


class ComputerRetrivAPIView(generics.RetrieveAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerRetrivSerializer
    lookup_field = "pk"

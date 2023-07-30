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


class ComputerGamingAPIView(generics.ListAPIView):
    queryset = Computer.objects.filter(computer_type=Computer.ComputerType.gaming)
    serializer_class = ComputerListSerializer


class ComputerHomeAPIView(generics.ListAPIView):
    queryset = Computer.objects.filter(computer_type=Computer.ComputerType.home)
    serializer_class = ComputerListSerializer


class ComputerAllInOneAPIView(generics.ListAPIView):
    queryset = Computer.objects.filter(computer_type=Computer.ComputerType.all_in_one)
    serializer_class = ComputerListSerializer

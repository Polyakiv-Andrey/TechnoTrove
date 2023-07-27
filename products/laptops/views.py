from rest_framework import generics

from products.laptops.models import Laptop
from products.laptops.serializers import LaptopListSerializer, LaptopRetrivSerializer


class LaptopListAPIVIew(generics.ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopListSerializer


class LaptopRetrivAPIView(generics.RetrieveAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopRetrivSerializer
    lookup_field = "pk"


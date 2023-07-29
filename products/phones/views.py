from rest_framework import generics

from products.phones.models import Phone
from products.phones.serializers import PhoneRetrivSerializer, PhoneListSerializer


class PhoneListAPIVIew(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneListSerializer


class PhoneRetrivAPIView(generics.RetrieveAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneRetrivSerializer
    lookup_field = "pk"

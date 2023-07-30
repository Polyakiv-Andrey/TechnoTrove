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


class PhoneSamsungAPIView(generics.ListAPIView):
    queryset = Phone.objects.filter(phone_type=Phone.PhoneType.samsung)
    serializer_class = PhoneListSerializer


class PhoneGoogleAPIView(generics.ListAPIView):
    queryset = Phone.objects.filter(phone_type=Phone.PhoneType.google)
    serializer_class = PhoneListSerializer


class PhoneIPhoneAPIView(generics.ListAPIView):
    queryset = Phone.objects.filter(phone_type=Phone.PhoneType.iphone)
    serializer_class = PhoneListSerializer


class PhoneOnePlusAPIView(generics.ListAPIView):
    queryset = Phone.objects.filter(phone_type=Phone.PhoneType.one_plus)
    serializer_class = PhoneListSerializer

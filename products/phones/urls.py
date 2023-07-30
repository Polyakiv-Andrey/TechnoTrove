from django.urls import path

from products.phones.views import (
    PhoneListAPIVIew,
    PhoneRetrivAPIView,
    PhoneSamsungAPIView,
    PhoneGoogleAPIView,
    PhoneIPhoneAPIView,
    PhoneOnePlusAPIView
)

app_name = "phones"

urlpatterns = [
    path("", PhoneListAPIVIew.as_view(), name="phone-list"),
    path("<int:pk>/", PhoneRetrivAPIView.as_view(), name="phone-ditail"),
    path("samsung/", PhoneSamsungAPIView.as_view(), name="phone-samsung"),
    path("google/", PhoneGoogleAPIView.as_view(), name="phone-google"),
    path("iphone/", PhoneIPhoneAPIView.as_view(), name="phone-iphone"),
    path("one-plus/", PhoneOnePlusAPIView.as_view(), name="phone-one-plus"),
]

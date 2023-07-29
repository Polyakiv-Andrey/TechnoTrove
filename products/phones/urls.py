from django.urls import path

from products.phones.views import PhoneListAPIVIew, PhoneRetrivAPIView

app_name = "phones"

urlpatterns = [
    path("", PhoneListAPIVIew.as_view(), name="phone-list"),
    path("<int:pk>/", PhoneRetrivAPIView.as_view(), name="phone-ditail")
]

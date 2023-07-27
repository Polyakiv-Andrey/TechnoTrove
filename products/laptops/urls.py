from django.urls import path

from products.laptops.views import LaptopListAPIVIew, LaptopRetrivAPIView

app_name = "laptops"

urlpatterns = [
    path("", LaptopListAPIVIew.as_view(), name="laptop-list"),
    path("<int:pk>/", LaptopRetrivAPIView.as_view(), name="laptop-ditail")
]


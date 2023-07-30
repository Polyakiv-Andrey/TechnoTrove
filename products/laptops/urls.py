from django.urls import path

from products.laptops.views import (
    LaptopListAPIVIew,
    LaptopRetrivAPIView,
    LaptopGamingAPIView,
    LaptopMacBooksAPIView,
    LaptopChromeBooksAPIView
)

app_name = "laptops"

urlpatterns = [
    path("", LaptopListAPIVIew.as_view(), name="laptop-list"),
    path("<int:pk>/", LaptopRetrivAPIView.as_view(), name="laptop-ditail"),
    path("geming/", LaptopGamingAPIView.as_view(), name="laptop-gaming"),
    path("mac-book/", LaptopMacBooksAPIView.as_view(), name="laptop-mac-book"),
    path("chrome-book/", LaptopChromeBooksAPIView.as_view(), name="laptop-chrome-book")
]


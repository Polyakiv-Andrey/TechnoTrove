from django.urls import path

from products.computers.views import (
    ComputerListAPIVIew,
    ComputerRetrivAPIView,
    ComputerGamingAPIView,
    ComputerHomeAPIView,
    ComputerAllInOneAPIView
)

app_name = "computer"

urlpatterns = [
    path("", ComputerListAPIVIew.as_view(), name="computer-list"),
    path("<int:pk>/", ComputerRetrivAPIView.as_view(), name="computer-ditail"),
    path("geming/", ComputerGamingAPIView.as_view(), name="computer-gaming"),
    path("home/", ComputerHomeAPIView.as_view(), name="computer-home"),
    path("all-in-one/", ComputerAllInOneAPIView.as_view(), name="all-in-one-computer")
]

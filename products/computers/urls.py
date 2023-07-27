from django.urls import path

from products.computers.views import ComputerListAPIVIew, ComputerRetrivAPIView

app_name = "computer"

urlpatterns = [
    path("", ComputerListAPIVIew.as_view(), name="computer-list"),
    path("<int:pk>/", ComputerRetrivAPIView.as_view(), name="computer-ditail")
]
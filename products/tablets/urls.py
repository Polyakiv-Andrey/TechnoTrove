from django.urls import path

from products.tablets.views import TabletsListAPIVIew, TabletsRetrivAPIView

app_name = "tablets"

urlpatterns = [
    path("", TabletsListAPIVIew.as_view(), name="tablets-list"),
    path("<int:pk>/", TabletsRetrivAPIView.as_view(), name="tablets-ditail")
]
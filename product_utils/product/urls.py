from django.urls import path, include

app_name = "product"

urlpatterns = [
    path("laptops/", include("products.laptops.urls", namespace="laptops")),
    path("computers/", include("products.computers.urls", namespace="computers")),
    path("monitors/", include("products.monitors.urls", namespace="monitors")),
]


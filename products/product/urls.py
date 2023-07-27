from django.urls import path, include

app_name = "product"

urlpatterns = [
    path("laptops/", include("products.laptops.urls", namespace="laptops"))
]


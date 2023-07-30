from django.urls import path

from products.tablets.views import (
    TabletsListAPIVIew,
    TabletsRetrivAPIView,
    TabletsAndroidAPIView,
    TabletsIPadsAPIView,
    TabletsSurfaceAPIView
)

app_name = "tablets"

urlpatterns = [
    path("", TabletsListAPIVIew.as_view(), name="tablet-list"),
    path("<int:pk>/", TabletsRetrivAPIView.as_view(), name="tablet-ditail"),
    path("android/", TabletsAndroidAPIView.as_view(), name="tablet-android"),
    path("ipads/", TabletsIPadsAPIView.as_view(), name="tablet-ipads"),
    path("surface/", TabletsSurfaceAPIView.as_view(), name="tablet-surface")
]

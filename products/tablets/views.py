from rest_framework import generics

from products.tablets.models import Tablets
from products.tablets.serializers import TabletListSerializer, TabletsRetrivSerializer


class TabletsListAPIVIew(generics.ListAPIView):
    queryset = Tablets.objects.all()
    serializer_class = TabletListSerializer


class TabletsRetrivAPIView(generics.RetrieveAPIView):
    queryset = Tablets.objects.all()
    serializer_class = TabletsRetrivSerializer
    lookup_field = "pk"

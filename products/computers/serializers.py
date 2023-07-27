from products.computers.models import Computer
from products.laptops.serializers import LaptopRetrivSerializer
from products.product.serializers import ProductListSerializer


class ComputerListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Computer


class ComputerRetrivSerializer(LaptopRetrivSerializer):

    class Meta(LaptopRetrivSerializer.Meta):
        model = Computer

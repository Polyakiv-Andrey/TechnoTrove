from product_utils.components_of_device.serializers import (
    computer_processor_serializer,
    computer_memory_serializer,
    computer_graphics_serializer,
    computer_ports_serializer,
    computer_chassis_serializer
)
from products.computers.models import Computer
from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer


class ComputerListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Computer


class ComputerRetrivSerializer(ProductRetrivSerializer):
    processor = computer_processor_serializer
    memory = computer_memory_serializer
    graphics = computer_graphics_serializer
    ports_and_connectivity = computer_ports_serializer
    chassis = computer_chassis_serializer

    class Meta:
        model = Computer
        fields = ProductRetrivSerializer.Meta.fields + [
            "operating_system", "processor", "memory", "ssd_capacity", "graphics",
            "ports_and_connectivity", "chassis"
        ]


from product_utils.components_of_device.serializers import (
    display_serializer,
    battery_serializer,
    processor_serializer,
    memory_serializer,
    graphics_serializer,
    keyboard_serializer,
    ports_and_connectivity_serializer,
    chassis_serializer
)
from products.laptops.models import Laptop
from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer


class LaptopListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Laptop


class LaptopRetrivSerializer(ProductRetrivSerializer):
    display = display_serializer
    battery = battery_serializer
    processor = processor_serializer
    memory = memory_serializer
    graphics = graphics_serializer
    keyboard = keyboard_serializer
    ports_and_connectivity = ports_and_connectivity_serializer
    chassis = chassis_serializer

    class Meta:
        model = Laptop
        fields = ProductRetrivSerializer.Meta.fields + [
            "display", "battery", "processor", "memory", "ssd_capacity", "graphics",
            "keyboard", "ports_and_connectivity", "chassis", "operating_system"
        ]

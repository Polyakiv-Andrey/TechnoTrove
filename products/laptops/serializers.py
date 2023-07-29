from product_utils.components_of_device.serializers import (
    laptop_display_serializer,
    laptop_battery_serializer,
    laptop_processor_serializer,
    laptop_memory_serializer,
    laptop_graphics_serializer,
    laptop_keyboard_serializer,
    laptop_ports_and_connectivity_serializer,
    laptop_chassis_serializer
)
from products.laptops.models import Laptop
from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer


class LaptopListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Laptop


class LaptopRetrivSerializer(ProductRetrivSerializer):
    display = laptop_display_serializer
    battery = laptop_battery_serializer
    processor = laptop_processor_serializer
    memory = laptop_memory_serializer
    graphics = laptop_graphics_serializer
    keyboard = laptop_keyboard_serializer
    ports_and_connectivity = laptop_ports_and_connectivity_serializer
    chassis = laptop_chassis_serializer

    class Meta:
        model = Laptop
        fields = ProductRetrivSerializer.Meta.fields + [
            "display", "battery", "processor", "memory", "ssd_capacity", "graphics",
            "keyboard", "ports_and_connectivity", "chassis", "operating_system"
        ]

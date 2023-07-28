from products.components_of_device.serializers import *
from products.laptops.models import Laptop
from products.product.models import Image
from products.product.serializers import ProductListSerializer


class LaptopListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Laptop


class LaptopRetrivSerializer(serializers.ModelSerializer):
    additional_images = serializers.SerializerMethodField()
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
        fields = ProductListSerializer.Meta.fields + [
            "product_description", "SKU", "additional_images", "condition", "warranty",
            "display", "battery", "processor", "memory", "ssd_capacity", "graphics",
            "keyboard", "ports_and_connectivity", "chassis", "operating_system"
        ]

    def get_additional_images(self, laptop):
        image_ids = laptop.additional_images.values_list('id', flat=True)
        images = Image.objects.filter(id__in=image_ids)
        return [image.image.url for image in images]

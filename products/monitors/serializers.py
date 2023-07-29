from rest_framework import serializers

from product_utils.components_of_device.serializers import (
    monitor_key_specification_serializer,
    monitor_features_serializer,
    monitor_display_serializer,
    monitor_physical_serializer,
    monitor_ergonomics_serializer,
    monitors_ports_serializer
)
from products.monitors.models import Monitor
from product_utils.product.models import Image
from product_utils.product.serializers import ProductListSerializer


class MonitorListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Monitor


class MonitorRetrivSerializer(serializers.ModelSerializer):
    key_specification = monitor_key_specification_serializer
    features = monitor_features_serializer
    display = monitor_display_serializer
    physical = monitor_physical_serializer
    ergonomics = monitor_ergonomics_serializer
    ports = monitors_ports_serializer

    class Meta:
        model = Monitor
        fields = ProductListSerializer.Meta.fields + [
            "product_description", "SKU", "additional_images", "condition", "warranty",
            "key_specification", "features", "display", "physical", "ergonomics", "ports",
        ]

    def get_additional_images(self, laptop):
        image_ids = laptop.additional_images.values_list('id', flat=True)
        images = Image.objects.filter(id__in=image_ids)
        return [image.image.url for image in images]


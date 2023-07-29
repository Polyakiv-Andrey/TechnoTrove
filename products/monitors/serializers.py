from product_utils.components_of_device.serializers import (
    monitor_key_specification_serializer,
    monitor_features_serializer,
    monitor_display_serializer,
    monitor_physical_serializer,
    monitor_ergonomics_serializer,
    monitors_ports_serializer
)
from products.monitors.models import Monitor
from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer


class MonitorListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Monitor


class MonitorRetrivSerializer(ProductRetrivSerializer):
    key_specification = monitor_key_specification_serializer
    features = monitor_features_serializer
    display = monitor_display_serializer
    physical = monitor_physical_serializer
    ergonomics = monitor_ergonomics_serializer
    ports = monitors_ports_serializer

    class Meta:
        model = Monitor
        fields = ProductRetrivSerializer.Meta.fields + [
            "key_specification", "features", "display", "physical", "ergonomics", "ports",
        ]

from product_utils.components_of_device.serializers import (
    tablet_overview,
    tablet_ports_serializer,
    tablet_key_spec_serializer,
    tablet_dimensions_serializer,
    tablet_battery_serializer,
    tablet_camera_serializer,
)
from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer
from products.tablets.models import Tablets


class TabletListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Tablets


class TabletsRetrivSerializer(ProductRetrivSerializer):
    overview = tablet_overview
    ports_and_connectivity = tablet_ports_serializer
    key_spec = tablet_key_spec_serializer
    dimensions = tablet_dimensions_serializer
    battery = tablet_battery_serializer
    camera = tablet_camera_serializer

    class Meta:
        model = Tablets
        fields = ProductRetrivSerializer.Meta.fields + [
            "overview", "ports_and_connectivity", "key_spec", "dimensions", "battery", "camera",
        ]

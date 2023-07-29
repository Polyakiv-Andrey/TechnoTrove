from product_utils.components_of_device.serializers import (
    phone_overview_serializer,
    phone_display_serializer,
    phone_camera_serializer,
    phone_dimensions_serializer,
    phone_storage_serializer,
    phone_connectivity_serializer,
    phone_power_serializer,
    phone_technical_specifications_serializer
)

from product_utils.product.serializers import ProductListSerializer, ProductRetrivSerializer
from products.phones.models import Phone


class PhoneListSerializer(ProductListSerializer):

    class Meta(ProductListSerializer.Meta):
        model = Phone


class PhoneRetrivSerializer(ProductRetrivSerializer):
    overview = phone_overview_serializer
    display = phone_display_serializer
    camera = phone_camera_serializer
    dimensions = phone_dimensions_serializer
    storage = phone_storage_serializer
    connectivity = phone_connectivity_serializer
    power = phone_power_serializer
    technical_specifications = phone_technical_specifications_serializer

    class Meta:
        model = Phone
        fields = ProductRetrivSerializer.Meta.fields + [
            "overview", "display", "camera", "dimensions", "storage",
            "connectivity", "power", "technical_specifications"
        ]

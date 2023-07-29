from django.db import models

from product_utils.components_of_device.models import (
    TabletsOverview,
    TabletsPortsAndConnectivity,
    TabletsKeySpec,
    TabletsDimensions,
    TabletsBattery,
    TabletCamera
)
from product_utils.product.models import Product


class Tablets(Product):
    overview = models.OneToOneField(
        TabletsOverview,
        on_delete=models.CASCADE,
        related_name="tablet_overview",
        blank=True,
        null=True
    )
    ports_and_connectivity = models.OneToOneField(
        TabletsPortsAndConnectivity,
        on_delete=models.CASCADE,
        related_name="tablet_ports",
        blank=True,
        null=True
    )
    key_spec = models.OneToOneField(
        TabletsKeySpec,
        on_delete=models.CASCADE,
        related_name="tablet_key_spec",
        blank=True,
        null=True
    )
    dimensions = models.OneToOneField(
        TabletsDimensions,
        on_delete=models.CASCADE,
        related_name="tablet_dimensions",
        blank=True,
        null=True
    )
    battery = models.OneToOneField(
        TabletsBattery,
        on_delete=models.CASCADE,
        related_name="tablet_battery",
        blank=True,
        null=True
    )
    camera = models.OneToOneField(
        TabletCamera,
        on_delete=models.CASCADE,
        related_name="tablet_camera",
        blank=True,
        null=True
    )

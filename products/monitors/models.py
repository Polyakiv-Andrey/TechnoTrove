from django.db import models

from product_utils.components_of_device.models import (
    MonitorKeySpecification,
    MonitorFeatures,
    MonitorDisplay,
    MonitorPhysical,
    MonitorErgonomics,
    MonitorPorts
)
from product_utils.product.models import Product


class Monitor(Product):
    key_specification = models.OneToOneField(
        MonitorKeySpecification,
        on_delete=models.CASCADE,
        related_name="key_specification",
        blank=True,
        null=True
    )
    features = models.OneToOneField(
        MonitorFeatures,
        on_delete=models.CASCADE,
        related_name="features",
        blank=True,
        null=True
    )
    display = models.OneToOneField(
        MonitorDisplay,
        on_delete=models.CASCADE,
        related_name="monitor_display",
        blank=True,
        null=True
    )
    physical = models.OneToOneField(
        MonitorPhysical,
        on_delete=models.CASCADE,
        related_name="physical",
        blank=True,
        null=True
    )
    ergonomics = models.OneToOneField(
        MonitorErgonomics,
        on_delete=models.CASCADE,
        related_name="ergonomics",
        blank=True,
        null=True
    )
    ports = models.OneToOneField(
        MonitorPorts,
        on_delete=models.CASCADE,
        related_name="monitors_ports",
        blank=True,
        null=True
    )


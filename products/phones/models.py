from django.db import models

from product_utils.components_of_device.models import (
    PhoneOverview,
    PhoneDisplay,
    PhoneCamera,
    PhoneDimensions,
    PhoneStorage,
    PhoneConnectivity,
    PhonePower,
    PhoneTechnicalSpecifications
)
from product_utils.product.models import Product


class Phone(Product):
    overview = models.OneToOneField(
        PhoneOverview,
        on_delete=models.CASCADE,
        related_name="phone_overview",
        blank=True,
        null=True
    )
    display = models.OneToOneField(
        PhoneDisplay,
        on_delete=models.CASCADE,
        related_name="phone_display",
        blank=True,
        null=True
    )
    camera = models.OneToOneField(
        PhoneCamera,
        on_delete=models.CASCADE,
        related_name="phone_camera",
        blank=True,
        null=True
    )
    dimensions = models.OneToOneField(
        PhoneDimensions,
        on_delete=models.CASCADE,
        related_name="phone_dimensions",
        blank=True,
        null=True
    )
    storage = models.OneToOneField(
        PhoneStorage,
        on_delete=models.CASCADE,
        related_name="phone_storage",
        blank=True,
        null=True
    )
    connectivity = models.OneToOneField(
        PhoneConnectivity,
        on_delete=models.CASCADE,
        related_name="phone_connectivity",
        blank=True,
        null=True
    )
    power = models.OneToOneField(
        PhonePower,
        on_delete=models.CASCADE,
        related_name="phone_power",
        blank=True,
        null=True
    )
    technical_specifications = models.OneToOneField(
        PhoneTechnicalSpecifications,
        on_delete=models.CASCADE,
        related_name="phone_technical_specifications",
        blank=True,
        null=True
    )

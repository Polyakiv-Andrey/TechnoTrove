from django.db import models

from product_utils.components_of_device.models import (
    Display,
    Battery,
    Processor,
    Memory,
    Graphics,
    Keyboard,
    PortsAndConnectivity,
    Chassis
)
from product_utils.product.models import Product


class Laptop(Product):

    display = models.OneToOneField(
        Display, on_delete=models.CASCADE, related_name="display", blank=True, null=True
    )
    battery = models.OneToOneField(
        Battery, on_delete=models.CASCADE, related_name="battery", blank=True, null=True
    )
    processor = models.OneToOneField(
        Processor, on_delete=models.CASCADE, related_name="processor", blank=True, null=True
    )
    memory = models.OneToOneField(
        Memory, on_delete=models.CASCADE, related_name="memory", blank=True, null=True
    )
    ssd_capacity = models.IntegerField(blank=True, null=True, default=0)
    graphics = models.OneToOneField(
        Graphics, on_delete=models.CASCADE, related_name="graphics", blank=True, null=True
    )
    keyboard = models.OneToOneField(
        Keyboard, on_delete=models.CASCADE, related_name="keyboard", blank=True, null=True
    )
    ports_and_connectivity = models.OneToOneField(
        PortsAndConnectivity, on_delete=models.CASCADE, related_name="ports", blank=True, null=True
    )
    chassis = models.OneToOneField(Chassis, on_delete=models.CASCADE, related_name="chassis")
    operating_system = models.CharField(max_length=50, blank=True, null=True)

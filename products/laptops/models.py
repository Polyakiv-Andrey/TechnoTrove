from django.db import models

from product_utils.components_of_device.models import (
    LaptopDisplay,
    LaptopBattery,
    LaptopProcessor,
    LaptopMemory,
    LaptopGraphics,
    LaptopKeyboard,
    LaptopPortsAndConnectivity,
    LaptopChassis
)
from product_utils.product.models import Product


class Laptop(Product):

    display = models.OneToOneField(
        LaptopDisplay, on_delete=models.CASCADE, related_name="display", blank=True, null=True
    )
    battery = models.OneToOneField(
        LaptopBattery, on_delete=models.CASCADE, related_name="battery", blank=True, null=True
    )
    processor = models.OneToOneField(
        LaptopProcessor, on_delete=models.CASCADE, related_name="processor", blank=True, null=True
    )
    memory = models.OneToOneField(
        LaptopMemory, on_delete=models.CASCADE, related_name="memory", blank=True, null=True
    )
    ssd_capacity = models.IntegerField(blank=True, null=True, default=0)
    graphics = models.OneToOneField(
        LaptopGraphics, on_delete=models.CASCADE, related_name="graphics", blank=True, null=True
    )
    keyboard = models.OneToOneField(
        LaptopKeyboard, on_delete=models.CASCADE, related_name="keyboard", blank=True, null=True
    )
    ports_and_connectivity = models.OneToOneField(
        LaptopPortsAndConnectivity, on_delete=models.CASCADE, related_name="ports", blank=True, null=True
    )
    chassis = models.OneToOneField(LaptopChassis, on_delete=models.CASCADE, related_name="chassis")
    operating_system = models.CharField(max_length=50, blank=True, null=True)

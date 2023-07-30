import django
from django.db import models

from product_utils.components_of_device.models import (
    ComputerProcessor,
    ComputerMemory,
    ComputerGraphics,
    ComputerPortsAndConnectivity,
    ComputerChassis
)
from product_utils.product.models import Product


class Computer(Product):
    operating_system = models.CharField(max_length=50, blank=True, null=True)
    processor = models.OneToOneField(
        ComputerProcessor,
        on_delete=models.CASCADE,
        related_name="computer_processor",
        blank=True,
        null=True
    )
    memory = models.OneToOneField(
        ComputerMemory,
        on_delete=models.CASCADE,
        related_name="computer_memory",
        blank=True,
        null=True
    )
    ssd_capacity = models.IntegerField(blank=True, null=True)
    graphics = models.OneToOneField(
        ComputerGraphics,
        on_delete=models.CASCADE,
        related_name="computer_graphics",
        blank=True,
        null=True
    )
    ports_and_connectivity = models.OneToOneField(
        ComputerPortsAndConnectivity,
        on_delete=models.CASCADE,
        related_name="computer_ports",
        blank=True,
        null=True
    )
    chassis = models.OneToOneField(
        ComputerChassis,
        on_delete=models.CASCADE,
        related_name="computer_chassis",
        blank=True,
        null=True
    )

    class ComputerType:
        gaming = "Gaming"
        home = "Home"
        all_in_one = "All_in_one"

    COMPUTER_TYPES = (
        (ComputerType.gaming, "Gaming"),
        (ComputerType.home, "Home"),
        (ComputerType.all_in_one, "All_in_one")
    )
    computer_type = models.CharField(
        max_length=20,
        choices=COMPUTER_TYPES,
        default=ComputerType.home,
        blank=True,
        null=True
    )

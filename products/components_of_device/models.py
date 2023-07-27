from django.db import models


class Display(models.Model):
    screen_size = models.CharField(max_length=30, blank=True, null=True)
    resolution = models.CharField(max_length=30, blank=True, null=True)
    refresh_rate = models.IntegerField(blank=True, null=True)
    screen_type = models.CharField(max_length=30, blank=True, null=True)
    brightness = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"display id: {self.id}"


class Battery(models.Model):
    run_time = models.IntegerField(blank=True, null=True)
    technology = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"battery id: {self.id}"


class Processor(models.Model):
    manufacturer = models.CharField(max_length=30, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    clock_speed = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    boost_frequency = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f"processor id: {self.id}"


class Memory(models.Model):
    installed_size = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"memory id: {self.id}"


class Graphics(models.Model):
    graphics_type = models.CharField(max_length=50, blank=True, null=True)
    graphics_manufacturer = models.CharField(max_length=100, blank=True, null=True)
    graphics_card = models.CharField(max_length=100, blank=True, null=True)
    integrated_graphics = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"graphics id: {self.id}"


class Keyboard(models.Model):
    backlit_keyboard = models.BooleanField(default=False, blank=True, null=True)
    numeric_keyboard = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"keyboard id: {self.id}"


class PortsAndConnectivity(models.Model):
    usb_3_0 = models.IntegerField(default=0, blank=True, null=True)
    usb_c = models.IntegerField(default=0, blank=True, null=True)
    hdmi = models.IntegerField(default=0, blank=True, null=True)
    wifi = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"ports and connectivity id: {self.id}"


class Chassis(models.Model):
    height = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    depth = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    optical_drive = models.CharField(max_length=50, blank=True, null=True)
    webcam = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"chassis id: {self.id}"

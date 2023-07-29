from rest_framework import serializers
from .models import *


MODELS_AND_SERIALIZERS = {
    LaptopDisplay: "LaptopDisplaySerializer",
    LaptopBattery: "LaptopBatterySerializer",
    LaptopProcessor: "LaptopProcessorSerializer",
    LaptopMemory: "LaptopMemorySerializer",
    LaptopGraphics: "LaptopGraphicsSerializer",
    LaptopKeyboard: "LaptopKeyboardSerializer",
    LaptopPortsAndConnectivity: "LaptopPortsAndConnectivitySerializer",
    LaptopChassis: "LaptopChassisSerializer",
    ComputerProcessor: "ComputerProcessorSerializer",
    ComputerMemory: "ComputerMemorySerializer",
    ComputerGraphics: "ComputerGraphicsSerializer",
    ComputerPortsAndConnectivity: "ComputerPortsAndConnectivitySerializer",
    ComputerChassis: "ComputerChassisSerializer",
    MonitorKeySpecification: "MonitorKeySpecificationSerializer",
    MonitorFeatures: "MonitorFeaturesSerializer",
    MonitorDisplay: "MonitorDisplaySerializer",
    MonitorPhysical: "MonitorPhysicalSerializer",
    MonitorErgonomics: "MonitorErgonomicsSerializer",
    MonitorPorts: "MonitorPortsSerializer",
    TabletsOverview: "TabletsOverviewSerializer",
    TabletsPortsAndConnectivity: "TabletsPortsAndConnectivitySerializer",
    TabletsKeySpec: "TabletsKeySpecSerializer",
    TabletsDimensions: "TabletsDimensionsSerializer",
    TabletsBattery: "TabletsBatterySerializer",
    TabletCamera: "TabletCameraSerializer",
    PhoneOverview: "PhoneOverviewSerializer",
    PhoneDisplay: "PhoneDisplaySerializer",
    PhoneCamera: "PhoneCameraSerializer",
    PhoneDimensions: "PhoneDimensionsSerializer",
    PhoneStorage: "PhoneStorageSSerializer",
    PhoneConnectivity: "PhoneConnectivitySerializer",
    PhonePower: "PhonePowerSerializer",
    PhoneTechnicalSpecifications: "PhoneTechnicalSpecificationsSerializer",
}


for model, serializer_name in MODELS_AND_SERIALIZERS.items():
    serializer_class = type(
        serializer_name,
        (serializers.ModelSerializer,),
        {
            "Meta":
                type(
                    "Meta",
                    (object,),
                    {"model": model, "fields": "__all__"}
                )
        }
    )
    locals()[serializer_name] = serializer_class

laptop_display_serializer = LaptopDisplaySerializer()
laptop_battery_serializer = LaptopBatterySerializer()
laptop_processor_serializer = LaptopProcessorSerializer()
laptop_memory_serializer = LaptopMemorySerializer()
laptop_graphics_serializer = LaptopGraphicsSerializer()
laptop_keyboard_serializer = LaptopKeyboardSerializer()
laptop_ports_and_connectivity_serializer = LaptopPortsAndConnectivitySerializer()
laptop_chassis_serializer = LaptopChassisSerializer()
computer_processor_serializer = ComputerProcessorSerializer()
computer_memory_serializer = ComputerMemorySerializer()
computer_graphics_serializer = ComputerGraphicsSerializer()
computer_ports_serializer = ComputerPortsAndConnectivitySerializer()
computer_chassis_serializer = ComputerChassisSerializer()
monitor_key_specification_serializer = MonitorKeySpecificationSerializer()
monitor_features_serializer = MonitorFeaturesSerializer()
monitor_display_serializer = MonitorDisplaySerializer()
monitor_physical_serializer = MonitorPhysicalSerializer()
monitor_ergonomics_serializer = MonitorErgonomicsSerializer()
monitors_ports_serializer = MonitorPortsSerializer()
tablet_overview = TabletsOverviewSerializer()
tablet_ports_serializer = TabletsPortsAndConnectivitySerializer()
tablet_key_spec_serializer = TabletsKeySpecSerializer()
tablet_dimensions_serializer = TabletsDimensionsSerializer()
tablet_battery_serializer = TabletsBatterySerializer()
tablet_camera_serializer = TabletCameraSerializer()
phone_overview_serializer = PhoneOverviewSerializer()
phone_display_serializer = PhoneDisplaySerializer()
phone_camera_serializer = PhoneCameraSerializer()
phone_dimensions_serializer = PhoneDimensionsSerializer()
phone_storage_serializer = PhoneStorageSSerializer()
phone_connectivity_serializer = PhoneConnectivitySerializer
phone_power_serializer = PhonePowerSerializer()
phone_technical_specifications_serializer = PhoneTechnicalSpecificationsSerializer()

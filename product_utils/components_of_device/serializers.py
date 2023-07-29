from rest_framework import serializers
from .models import *


MODELS_AND_SERIALIZERS = {
    Display: "DisplaySerializer",
    Battery: "BatterySerializer",
    Processor: "ProcessorSerializer",
    Memory: "MemorySerializer",
    Graphics: "GraphicsSerializer",
    Keyboard: "KeyboardSerializer",
    PortsAndConnectivity: "PortsAndConnectivitySerializer",
    Chassis: "ChassisSerializer",
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

display_serializer = DisplaySerializer()
battery_serializer = BatterySerializer()
processor_serializer = ProcessorSerializer()
memory_serializer = MemorySerializer()
graphics_serializer = GraphicsSerializer()
keyboard_serializer = KeyboardSerializer()
ports_and_connectivity_serializer = PortsAndConnectivitySerializer()
chassis_serializer = ChassisSerializer()
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

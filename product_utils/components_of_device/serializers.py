from rest_framework import serializers
from .models import (
    Display,
    Battery,
    Processor,
    Memory,
    Graphics,
    Keyboard,
    PortsAndConnectivity,
    Chassis,
    MonitorKeySpecification,
    MonitorFeatures,
    MonitorDisplay,
    MonitorPhysical,
    MonitorErgonomics,
    MonitorPorts,
    TabletsOverview,
    TabletsKeySpec,
    TabletsPortsAndConnectivity,
    TabletsDimensions,
    TabletsBattery,
    TabletCamera
)
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
    TabletCamera: "TabletCameraSerializer"
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

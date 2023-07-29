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
    MonitorPorts
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
    MonitorPorts: "MonitorPortsSerializer"
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

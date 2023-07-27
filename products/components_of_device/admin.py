from django.contrib import admin

import products.components_of_device.models


for component_name in dir(products.components_of_device.models):
    component = getattr(products.components_of_device.models, component_name)
    if hasattr(component, '_meta'):
        admin.site.register(component)

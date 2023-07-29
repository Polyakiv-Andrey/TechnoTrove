from django.contrib import admin

import product_utils.components_of_device.models as models

for component_name in dir(models):
    component = getattr(models, component_name)
    if hasattr(component, '_meta'):
        admin.site.register(component)

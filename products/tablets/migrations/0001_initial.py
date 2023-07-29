# Generated by Django 4.2.3 on 2023-07-29 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components_of_device', '0003_tabletcamera_tabletsbattery_tabletsdimensions_and_more'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tablets',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('battery', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_battery', to='components_of_device.tabletsbattery')),
                ('camera', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_camera', to='components_of_device.tabletcamera')),
                ('dimensions', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_dimensions', to='components_of_device.tabletsdimensions')),
                ('key_spec', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_key_spec', to='components_of_device.tabletskeyspec')),
                ('overview', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_overview', to='components_of_device.tabletsoverview')),
                ('ports_and_connectivity', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablet_ports', to='components_of_device.tabletsportsandconnectivity')),
            ],
            bases=('product.product',),
        ),
    ]

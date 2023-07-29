# Generated by Django 4.2.3 on 2023-07-29 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components_of_device', '0004_phonecamera_phoneconnectivity_phonedimensions_and_more'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('camera', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_camera', to='components_of_device.phonecamera')),
                ('connectivity', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_connectivity', to='components_of_device.phoneconnectivity')),
                ('dimensions', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_dimensions', to='components_of_device.phonedimensions')),
                ('display', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_display', to='components_of_device.phonedisplay')),
                ('overview', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_overview', to='components_of_device.phoneoverview')),
                ('power', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_power', to='components_of_device.phonepower')),
                ('storage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_storage', to='components_of_device.phonestorage')),
                ('technical_specifications', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_technical_specifications', to='components_of_device.phonetechnicalspecifications')),
            ],
            bases=('product.product',),
        ),
    ]
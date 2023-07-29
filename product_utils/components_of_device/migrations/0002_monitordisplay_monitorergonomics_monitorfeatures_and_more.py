# Generated by Django 4.2.3 on 2023-07-28 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components_of_device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorDisplay',
            fields=[
                ('display_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components_of_device.display')),
                ('aspect_ratio', models.CharField(blank=True, max_length=30, null=True)),
                ('panel_type', models.CharField(blank=True, max_length=60, null=True)),
                ('display_type', models.CharField(blank=True, max_length=70, null=True)),
                ('vertical_viewing_angle', models.IntegerField(blank=True, null=True)),
                ('horizontal_viewing_angle', models.IntegerField(blank=True, null=True)),
                ('TFT_technology', models.CharField(blank=True, max_length=50, null=True)),
                ('image_contrast_ratio', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('components_of_device.display',),
        ),
        migrations.CreateModel(
            name='MonitorErgonomics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_adjustment', models.BooleanField(blank=True, default=False, null=True)),
                ('tilt', models.BooleanField(blank=True, default=False, null=True)),
                ('pivot', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_sync', models.BooleanField(blank=True, default=False, null=True)),
                ('hdr', models.BooleanField(blank=True, default=False, null=True)),
                ('speakers', models.BooleanField(blank=True, default=False, null=True)),
                ('console_compatibility', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorKeySpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_size', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('maximum_resolution', models.CharField(blank=True, max_length=20, null=True)),
                ('hdmi_type', models.CharField(blank=True, max_length=20, null=True)),
                ('aspect_ratio', models.CharField(blank=True, max_length=20, null=True)),
                ('panel_type', models.CharField(blank=True, max_length=40, null=True)),
                ('refresh_rate', models.IntegerField(blank=True, null=True)),
                ('response_time', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorPhysical',
            fields=[
                ('chassis_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components_of_device.chassis')),
                ('wall_mounting', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('components_of_device.chassis',),
        ),
        migrations.CreateModel(
            name='MonitorPorts',
            fields=[
                ('portsandconnectivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components_of_device.portsandconnectivity')),
                ('display_port', models.IntegerField(blank=True, default=0, null=True)),
                ('mini_display_port', models.IntegerField(blank=True, default=0, null=True)),
                ('HDMI_type', models.CharField(blank=True, max_length=30, null=True)),
                ('VGA', models.IntegerField(blank=True, default=0, null=True)),
                ('DVI', models.IntegerField(blank=True, default=0, null=True)),
            ],
            bases=('components_of_device.portsandconnectivity',),
        ),
    ]

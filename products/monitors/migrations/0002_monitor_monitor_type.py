# Generated by Django 4.2.3 on 2023-07-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='monitor_type',
            field=models.CharField(blank=True, choices=[('Gaming', 'Gaming'), ('4K', '4K'), ('Ultra_wide', 'Ultra_wide')], default='4K', max_length=20, null=True),
        ),
    ]
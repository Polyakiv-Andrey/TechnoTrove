# Generated by Django 4.2.3 on 2023-07-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='phone_type',
            field=models.CharField(blank=True, choices=[('iPhone', 'iPhone'), ('Samsung', 'Samsung'), ('Google', 'Google'), ('OnePlus', 'OnePlus')], default='Samsung', max_length=20, null=True),
        ),
    ]
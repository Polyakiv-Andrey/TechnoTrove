# Generated by Django 4.2.3 on 2023-07-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('new', 'new'), ('used', 'used')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
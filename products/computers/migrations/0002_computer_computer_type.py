# Generated by Django 4.2.3 on 2023-07-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='computer_type',
            field=models.CharField(blank=True, choices=[('Gaming', 'Gaming'), ('Home', 'Home'), ('All_in_one', 'All_in_one')], default='Home', max_length=20, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="fuel_type", field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="car",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]

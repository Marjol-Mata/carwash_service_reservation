# Generated by Django 5.0.3 on 2024-03-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0012_alter_car_car_photo_alter_car_car_photo_1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_photo",
            field=models.ImageField(blank=True, upload_to="photos/car_photos"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_1",
            field=models.ImageField(blank=True, upload_to="photos/car_photos"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_2",
            field=models.ImageField(blank=True, upload_to="photos/car_photos"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_3",
            field=models.ImageField(blank=True, upload_to="photos/car_photos"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_4",
            field=models.ImageField(blank=True, upload_to="photos/car_photos"),
        ),
    ]

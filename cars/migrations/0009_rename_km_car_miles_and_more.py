# Generated by Django 5.0.3 on 2024-03-24 11:09

import datetime
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0008_alter_car_features"),
    ]

    operations = [
        migrations.RenameField(model_name="car", old_name="km", new_name="miles",),
        migrations.RenameField(
            model_name="car", old_name="no_of_owners", new_name="no_of_owner",
        ),
        migrations.RenameField(
            model_name="car", old_name="vin_no", new_name="vin_number",
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo",
            field=models.ImageField(upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_1",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_2",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_3",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_photo_4",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="car",
            name="created_date",
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="car",
            name="doors",
            field=models.CharField(
                choices=[("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="features",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Cruise Control", "Cruise Control"),
                    ("Audio Interface", "Audio Interface"),
                    ("Airbags", "Airbags"),
                    ("Air Conditioning", "Air Conditioning"),
                    ("Seat Heating", "Seat Heating"),
                    ("Alarm System", "Alarm System"),
                    ("ParkAssist", "ParkAssist"),
                    ("Power Steering", "Power Steering"),
                    ("Reversing Camera", "Reversing Camera"),
                    ("Direct Fuel Injection", "Direct Fuel Injection"),
                    ("Auto Start/Stop", "Auto Start/Stop"),
                    ("Wind Deflector", "Wind Deflector"),
                    ("Bluetooth Handset", "Bluetooth Handset"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="car", name="fuel_type", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="car",
            name="state",
            field=models.CharField(
                choices=[
                    ("AL", "Alabama"),
                    ("AK", "Alaska"),
                    ("AZ", "Arizona"),
                    ("AR", "Arkansas"),
                    ("CA", "California"),
                    ("CO", "Colorado"),
                    ("CT", "Connecticut"),
                    ("DE", "Delaware"),
                    ("DC", "District Of Columbia"),
                    ("FL", "Florida"),
                    ("GA", "Georgia"),
                    ("HI", "Hawaii"),
                    ("ID", "Idaho"),
                    ("IL", "Illinois"),
                    ("IN", "Indiana"),
                    ("IA", "Iowa"),
                    ("KS", "Kansas"),
                    ("KY", "Kentucky"),
                    ("LA", "Louisiana"),
                    ("ME", "Maine"),
                    ("MD", "Maryland"),
                    ("MA", "Massachusetts"),
                    ("MI", "Michigan"),
                    ("MN", "Minnesota"),
                    ("MS", "Mississippi"),
                    ("MO", "Missouri"),
                    ("MT", "Montana"),
                    ("NE", "Nebraska"),
                    ("NV", "Nevada"),
                    ("NH", "New Hampshire"),
                    ("NJ", "New Jersey"),
                    ("NM", "New Mexico"),
                    ("NY", "New York"),
                    ("NC", "North Carolina"),
                    ("ND", "North Dakota"),
                    ("OH", "Ohio"),
                    ("OK", "Oklahoma"),
                    ("OR", "Oregon"),
                    ("PA", "Pennsylvania"),
                    ("RI", "Rhode Island"),
                    ("SC", "South Carolina"),
                    ("SD", "South Dakota"),
                    ("TN", "Tennessee"),
                    ("TX", "Texas"),
                    ("UT", "Utah"),
                    ("VT", "Vermont"),
                    ("VA", "Virginia"),
                    ("WA", "Washington"),
                    ("WV", "West Virginia"),
                    ("WI", "Wisconsin"),
                    ("WY", "Wyoming"),
                ],
                max_length=100,
            ),
        ),
    ]

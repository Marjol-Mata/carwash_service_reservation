# Generated by Django 5.0.3 on 2024-03-22 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Teams", new_name="Team",),
    ]
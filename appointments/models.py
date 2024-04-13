from django.db import models
from datetime import datetime


# Create your models here.
class Booking(models.Model):
    your_name = models.CharField(max_length=100)
    your_phone = models.IntegerField()
    your_email = models.CharField(max_length=100)
    your_address = models.CharField(max_length=100)
    your_schedule = models.CharField(max_length=100)
    your_day = models.CharField(max_length=100)
    your_car = models.CharField(max_length=100)
    car_number = models.CharField(max_length=100, blank=True, null=True)
    your_message = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.user_id

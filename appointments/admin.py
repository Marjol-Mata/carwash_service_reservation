from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'your_phone', 'your_email', 'your_address', 'your_schedule', 'your_day', 'your_car')
    list_display_links = ('your_name', 'your_car')
    search_fields = ('your_name', 'your_phone', 'your_car', 'your_day')
    list_per_page = 25


admin.site.register(Booking, BookingAdmin)
from django.shortcuts import redirect
from django.contrib import messages
from .models import Booking
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_day = request.POST['your-day']
        your_car = request.POST['your-car']
        car_number = request.POST['car_number']
        subject = request.Post['subject']
        your_message = request.POST['your-message']
        user_id = request.POST['user-id']


        if request.user.is_authenticated:
            user_id = request.user.id
            has_booked = Booking.objects.all().filter(user_id=user_id, your_name=your_name, your_car=your_car, car_number=car_number).exists()
            if has_booked:
                messages.error(request, 'You have already made an Booking about this car. Please wait until we get back to you.')
                return redirect('appointments')

        booking = Booking(user_id=user_id, your_name=your_name, your_phone=your_phone, your_email=your_email, your_address=your_address,
                          your_schedule=your_schedule, your_day=your_day, your_car=your_car, car_number=car_number, subject=subject, your_message=your_message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Booking",
            f"You have a new Booking from the client. {user_id}, {your_name}, {your_car}, {car_number}, {subject}. Please login to your admin panel for more info.",
            "marjolmata29@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        booking.save()
        messages.success(request, 'Your request has been submitted, we will get bact to you shortly.')
        return redirect('appointments')

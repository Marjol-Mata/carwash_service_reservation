from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from pages.models import Team
from cars.models import Car
from appointments.models import Booking




def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        "teams": teams,
        "featured_cars": featured_cars,
        "all_cars": all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Motor Magic website regarding ' + subject
        message_body = 'Name: ' +name+ '. Email: ' +email+ ' Phone: ' +phone+ '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            "marjolmata29@gmail.com",
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('contact')

    return render(request, 'pages/contact.html')

def booking(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_schedule = request.POST['your-schedule']
        your_day = request.POST['your-day']
        your_message = request.POST['your-message']
        car_name = request.POST['car-name']
        car_number = request.POST['car-number']
        subject = request.POST['subject']

        email_subject = 'You have a new Booking from Motor Magic website regarding ' + subject + '.'
        message_body = ('Name: ' + your_name + '. Email: ' + your_email + ' Phone: ' + your_phone + '. Message: '
                        + your_message + '. Schedule: ' + your_schedule + '. Day: ' + your_day + '. Car Id: ' + car_number + '. Car Name: ' + car_name +'.')

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            "marjolmata29@gmail.com",
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('booking')

    return render(request, 'pages/booking.html')
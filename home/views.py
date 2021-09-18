from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'Variable1': "I am great",
        'Variable2': "Rohan is great"
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()

        # using alerts but you can still use the websites
        messages.success(request, 'Your query has been sent successfully')

    return render(request, 'contact.html')

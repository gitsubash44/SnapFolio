from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import about, Stat , Skill, ContactMessage, Service
from .models import Portfolio

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    portfolio = Portfolio.objects.all().order_by('order')
    services = Service.objects.all().order_by('order')  # Fetch services ordered by 'order'

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Your message has been sent successfully.")
            return HttpResponseRedirect(reverse('index') + '#contact')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "index.html", {
        'about': about_info,
        'stats': stats,
        'skills': skills,
        'portfolio': portfolio,
        'services': services  # Pass services to the template
    })
    

def ServiceDetailView(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, "service-details.html", {
        'service': service
    })
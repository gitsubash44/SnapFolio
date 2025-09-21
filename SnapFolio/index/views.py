from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import about, Stat , Skill, Contact
from .models import Portfolio

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    portfolio = Portfolio.objects.all().order_by('order')

    # Handle contact form
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect("index")  # reload same page after submission
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, "index.html", {
        'about': about_info,
        'stats': stats,
        'skills': skills,
        'portfolio': portfolio
    })
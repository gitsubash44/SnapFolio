from django.shortcuts import render
from .models import about, Stat , Skill
from .models import Portfolio

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    portfolio = Portfolio.objects.all().order_by('order')  # flat queryset for isotope

    return render(request, 'index.html', {
        'about': about_info,
        'stats': stats,
        'skills': skills,
        'portfolio': portfolio
    })
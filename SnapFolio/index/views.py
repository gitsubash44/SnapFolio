from django.shortcuts import render
from .models import about, Stat , Skill
from .models import Portfolio

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    # Group portfolios by category
    portfolios_by_category = {}
    for category_key, category_name in Portfolio.CATEGORY_CHOICES:
        portfolios_by_category[category_key] = Portfolio.objects.filter(category=category_key).order_by('order')
    return render(request, 'index.html', {
        'about': about_info,
        'stats': stats,
        'skills': skills,
        'portfolios_by_category': portfolios_by_category
    })

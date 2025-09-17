from django.shortcuts import render
from .models import about, Stat

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    return render(request, 'index.html', {'about': about_info, 'stats': stats})

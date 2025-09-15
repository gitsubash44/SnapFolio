from django.shortcuts import render
from .models import about

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_view(request):
    about_info = about.objects.first()
    return render(request, 'index.html', {'about': about_info})
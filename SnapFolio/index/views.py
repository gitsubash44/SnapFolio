from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import about, Stat , Skill, ContactMessage, Service, indexhero, MainArticle, SubArticle
from .models import Portfolio
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    about_info = about.objects.first()
    stats = Stat.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    portfolio = Portfolio.objects.all().order_by('order')
    services = Service.objects.all().order_by('order')  # Fetch services ordered by 'order'
    index_info = indexhero.objects.first()  # Fetch the first index object

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
        'services': services,  # Pass services to the template
        'index_info': {
            'title': index_info.title if index_info else "",
            'subtitle': index_info.subtitle if index_info else "",
            'description': index_info.description if index_info else "",
            'profile_image': index_info.profile_image.url if index_info and index_info.profile_image else "",
            'background_image': index_info.background_image.url if index_info and index_info.background_image else "",
        }  # Pass index information to the template
    })


def Services(request):
    services = Service.objects.all().order_by('order')
    return render(request, "services.html", {
        'services': services
    })


def ServiceDetailView(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, "service-details.html", {
        'service': service
    })
    


# Articles page — show all main topics
def articles(request):
    mains = MainArticle.objects.all()
    return render(request, "articles.html", {"mains": mains})


# Article Details — show sub-articles for a main topic
def article_details(request, main_id):
    main_article = get_object_or_404(MainArticle, id=main_id)
    sub_articles = SubArticle.objects.filter(main_article=main_article)
    return render(request, "article-details.html", {
        "main_article": main_article,
        "sub_articles": sub_articles
    })


# Article Read — show full content of a sub-article
def article_read(request, sub_id):
    sub_article = get_object_or_404(SubArticle, id=sub_id)
    sub_article.views += 1
    sub_article.save()
    related_articles = SubArticle.objects.filter(
        main_article=sub_article.main_article
    ).exclude(id=sub_id)[:3]

    return render(request, "article-read.html", {
        "sub_article": sub_article,
        "related_articles": related_articles
    })

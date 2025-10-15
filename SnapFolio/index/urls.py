from django.urls import path
from django.conf.urls.static import static

from SnapFolio import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.index, name="contact"),  # New URL pattern for contact form submission
    path("services/", views.Services, name="services"),  # Services page
    path("service/<int:service_id>/", views.ServiceDetailView, name="service_detail"),  # Service detail view
    path("articles/", views.articles, name="articles"),  # Articles page
    path("article-details/", views.article_details, name="article_detail"),  # Article details page
    path("article-read/", views.article_read, name="article_read"),  # Article read page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.conf.urls.static import static

from SnapFolio import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.index, name="contact"),  # New URL pattern for contact form submission
    path("service/<int:service_id>/", views.ServiceDetailView, name="service_detail"),  # Service detail view
    path("articles/", views.articles, name="articles"),  # Articles page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
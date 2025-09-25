from django.urls import path
from django.conf.urls.static import static

from SnapFolio import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.index, name="contact"),  # New URL pattern for contact form submission
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
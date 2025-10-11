from django.contrib import admin
from .models import about, Stat, Skill, Portfolio, ContactMessage, Service, indexhero
# Register your models here.
admin.site.register(about)
admin.site.register(Stat)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(ContactMessage)
admin.site.register(Service)
admin.site.register(indexhero)

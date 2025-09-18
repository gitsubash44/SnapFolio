from django.contrib import admin
from .models import about, Stat, Skill
# Register your models here.
admin.site.register(about)
admin.site.register(Stat)
admin.site.register(Skill)
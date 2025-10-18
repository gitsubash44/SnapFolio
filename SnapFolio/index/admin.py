from django.contrib import admin
from .models import about, Stat, Skill, Portfolio, ContactMessage, Service, indexhero, MainArticle, SubArticle
# Register your models here.
admin.site.register(about)
admin.site.register(Stat)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(ContactMessage)
admin.site.register(Service)
admin.site.register(indexhero)

class SubArticleInline(admin.TabularInline):
    model = SubArticle
    extra = 1

@admin.register(MainArticle)
class MainArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    inlines = [SubArticleInline]

@admin.register(SubArticle)
class SubArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_article', 'date_published', 'views')
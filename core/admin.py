from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ArticleAdmin(SummernoteModelAdmin):
    model = Article

class NewsAdmin(SummernoteModelAdmin):
    model = News


admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Specialization)
admin.site.register(Administration)
admin.site.register(News, NewsAdmin)
admin.site.register(CustomUser)
admin.site.register(Photo)
admin.site.register(Article, ArticleAdmin)



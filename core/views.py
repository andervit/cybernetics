from django.shortcuts import *
from .models import *
# Create your views here.
def home(request):
    news = News.objects.filter(published =True).order_by('-pub_date')[:2]
    return render(request, 'core/index.html', {'news':news})

def news(request):
    news = News.objects.filter(published=True)
    return render(request, 'core/all-news.html', {'news':news})

def new(request, id):
    new = News.objects.get(id=id)
    news = News.objects.filter(published=True).exclude(id=id)[0:2]
    return render(request, 'core/new.html', {'new':new, 'news':news})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article.html', {'article':article})

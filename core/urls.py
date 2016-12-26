from django.conf.urls import include, url
from core.views import *



urlpatterns = [
    url(r'^$', home, name="index"),
    url(r'^news$', news, name="news"),
    url(r'^news/(?P<id>[0-9]+)$', new, name='new'),
]

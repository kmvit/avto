from django.conf.urls import include, url
from views import *


urlpatterns = [
    url(r'^add/', NewsAdd.as_view(), name='news_add'),
    url(r'^category/(?P<slug>[\w-]+)/$', NewsCategory.as_view(), name='news_category'),
    url(r'^(?P<slug>[\w-]+)/$', Newsdetail.as_view(), name='newsdetail'),
    url(r'^$', Newslist.as_view(), name='newslist'),
]
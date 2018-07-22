from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^add/', ArticleAdd.as_view(), name='article_add'),
    url(r'^addfaq/', FaqAdd.as_view(), name='faq_add'),
    url(r'^faq/$', FaqList.as_view(), name='faq_list'),
    url(r'^faq/(?P<pk>\d+)/$', FaqDetail.as_view(), name='faq_detail'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/', Articledetail.as_view(), name='article_detail'),
    url(r'^$', Articlelist.as_view(), name='articlelist'),
]
from django.conf.urls import include, url
from django.contrib import admin
from school.views import *
from news.views import *
from articles.views import *
from school.models import *
from instructors.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dal import autocomplete
from footerpage.views import *
from city.models import *
from city.views import CityAutocomplete
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'school': SchoolSitemap,
    'instructor': InstructorSitemap,
    'news': NewsSitemap,
    'article': ArticleSitemap,
}





urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^city-autocomplete/$',CityAutocomplete.as_view(), name='city-autocomplete'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('profiles.urls', namespace='profiles', app_name='profiles')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),
    
    url(r'^city/', include('city.urls', namespace='city', app_name='city')),
    url(r'^school/', include('school.urls', namespace='school', app_name='school')),
    url(r'^news/', include('news.urls', namespace='news', app_name='news')),
    url(r'^article/', include('articles.urls', namespace='articles', app_name='articles')),
    url(r'^instructor/',  include('instructors.urls', namespace='instructor', app_name='instructor')),
    url(r'^tickets/', include("tickets.urls", namespace='tickets', app_name='tickets')),
    url(r'^quiz/',  include('quiz.urls', namespace='quiz', app_name='quiz')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
  

    url(r'^(?P<slug>[\w-]+)/$',  footerpage, name='footerpage'),
    

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

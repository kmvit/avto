from django.conf.urls import include, url
from school.views import *


app_name= 'school'
urlpatterns = [
    url(r'^addcity/$', add_city, name='addcity'),
    url(r'^sender/$', sender, name='xc'),
    url(r'^latest/feed/$', LatestSchoolsFeed()),
    url(r'^city/$', CitySearchList.as_view(), name='citysearchlist'),
    url(r'^documents/$', DocumentList.as_view(), name='document_list'),
    url(r'^reviewresponce/(?P<id>\d+)$', reviewresponce, name='reviewresponce'),
    url(r'^(?P<slug>[\w-]+)/feedback$', Feedbackschool.as_view(), name="feedbackschool"),
    url(r'^(?P<slug>[\w-]+)/success$', success, name="success"),
    url(r'^(?P<slug>[\w-]+)/foto/$', SchoolImageList.as_view(), name='fotolist'),
    url(r'^(?P<slug>[\w-]+)/document/$', SchoolDocumentList.as_view(), name='document_list'),
    url(r'^(?P<slug>[\w-]+)/reviews/$', ReviewsList.as_view(), name='reviewlist'),
    url(r'^(?P<slug>[\w-]+)/review/add$', ReviewAdd.as_view(), name='reviewadd'),
    url(r'^(?P<slug>[\w-]+)/review/reviewsend$', ReviewSend, name='reviewschoolsend'),
    url(r'^(?P<slug>[\w-]+)/verification/(?P<pk>\d+)$', ReviewVerificathion, name='review_verification'),
    url(r'^(?P<slug>[\w-]+)/address/$', BranchList.as_view(), name='branchlist'),
    url(r'^(?P<slug>[\w-]+)/onlineorder/$', FeedbackschoolList.as_view(), name='feedbackschool_list'),
    url(r'^(?P<slug>[\w-]+)/$', SchoolDetail.as_view(), name='schooldetail'),
    url(r'^$', SchoolList.as_view(), name='schoollist'),
]
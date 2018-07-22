from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', InstructorList.as_view(), name='instructorslist'),
    url(r'^reviewresponce/(?P<id>\d+)$', reviewresponce, name='reviewresponce'),
    url(r'^(?P<slug>[\w-]+)/feedback$', Feedback.as_view(), name="feedbackinstructor"),
    url(r'^(?P<slug>[\w-]+)/success$', success, name="success_instructor"),
    url(r'^(?P<slug>[\w-]+)/$', InstructorDetail.as_view(), name='instructordetail'),
    url(r'^(?P<slug>[\w-]+)/reviewinstructor/add$', ReviewInstructorAdd.as_view(), name='reviewinstructoradd'),
    url(r'^(?P<slug>[\w-]+)/reviewinstructor/reviewsend$', ReviewSend, name='reviewsend'),
    url(r'^(?P<slug>[\w-]+)/verification/(?P<pk>\d+)$', ReviewVerificathion, name='_instructor_review_verification'),
    url(r'^(?P<slug>[\w-]+)/onlineorder/$', FeedbackinstructorList.as_view(), name='feedbackinstructor_list'),
]
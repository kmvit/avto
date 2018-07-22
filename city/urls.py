from django.conf.urls import include, url
from views import *

app_name= 'city'
urlpatterns = [
      url(r'^redirect/$', redirect_city, name="redirect_city"),
      url(r'^(?P<slug>[\w-]+)/instructor/$', CityInstructorList.as_view(), name="city_instructor_list"),
      url(r'^(?P<slug>[\w-]+)/school/$', CitySchoolList.as_view(), name="city_school_list"),
     
]
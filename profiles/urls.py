from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile_detail'),
    url(r'^(?P<pk>\d+)/edit/$', update_profile, name='profile_update'),
    url(r'^(?P<pk>\d+)/schools/$', ProfileSchools.as_view(), name='profile_schools'),
    url(r'^(?P<pk>\d+)/schools/add/$', ProfileSchoolAdd.as_view(), name='profile_schools_add'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/edit/$', ProfileSchoolEdit.as_view(), name='profile_school_edit'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/editsocial/$', ProfileSchoolEditSocial.as_view(), name='profile_school_edit_social'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/delete/$', ProfileSchoolDelete.as_view(), name='profile_school_delete'),
    
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/branch/$', ProfileSchoolAdress.as_view(), name='profile_branch_list'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/branch/add/$', ProfileBranchAdd.as_view(), name='profile_branch_add'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/branch/edit/(?P<branch_pk>\d+)/$', ProfileBranchEdit.as_view(), name='profile_branch_edit'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/branch/delete/(?P<branch_pk>\d+)/$', ProfileBranchDelete.as_view(), name='profile_branch_delete'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/autodrome/add/$', ProfileAutodromeAdd.as_view(), name='profile_autodrome_add'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/autodrome/edit/(?P<autodrome_pk>\d+)/$', ProfileAutodromeEdit.as_view(), name='profile_autodrome_edit'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/autodrome/delete/(?P<autodrome_pk>\d+)/$', ProfileAutodromeDelete.as_view(), name='profile_autodrome_delete'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/schoolimage/$', ProfileSchoolImageList.as_view(), name='profile_schoolimage_list'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/schoolimage/add/$', ProfileSchoolImageAdd.as_view(), name='profile_schoolimage_add'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/schoolimage/delete/(?P<image_pk>\d+)/$', ProfileSchoolImageDelete.as_view(), name='profile_schoolimage_delete'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/schooldocuments/$', ProfileSchoolDocumentList.as_view(), name='profile_schooldocument_list'),
    url(r'^(?P<pk>\d+)/schools/(?P<slug>[\w-]+)/schooldocuments/add/$', ProfileSchoolDocumentAdd.as_view(), name='profile_schooldocument_add'),
    
    url(r'^(?P<pk>\d+)/instructors/$', ProfileInstructors.as_view(), name='profile_instructors'),
    url(r'^(?P<pk>\d+)/instructors/(?P<instructor_pk>\d+)/edit/$', ProfileInstructorsEdit.as_view(), name='profile_instructors_edit'),
    url(r'^(?P<pk>\d+)/instructors/add/$', ProfileInstructorAdd.as_view(), name='profile_instructor_add'),
    
    url(r'^(?P<pk>\d+)/bills/add/$', ProfileBillAdd.as_view(), name='profile_bill_add'),
]
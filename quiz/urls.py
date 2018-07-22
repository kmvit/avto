from django.conf.urls import url

from .views import *


urlpatterns = [
                        url(regex=r'^$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                        url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                        url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                        url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                        url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                        url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),
                           
                        url(regex=r'^fine/$',
                           view=FineList.as_view(),
                           name='fine_list'),
                           
                        url(regex=r'^rule/$',
                           view=RuleList.as_view(),
                           name='rule_list'),
                           
                        url(regex=r'^road/$',
                           view=RoadList.as_view(),
                           name='road_list'),
                           
                           
                        url(regex=r'^road-sings/$',
                           view=RoadSingList.as_view(),
                           name='roadsings_list'),
                        
                        url(regex=r'^road-sings/(?P<slug>[\w-]+)$',
                           view=RoadSingDetail.as_view(),
                           name='roadsings_detail'),
                        
                         url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=RegulView,
                           name='regul'),
                           
                        #  passes variable 'quiz_name' to quiz_take view
                        url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                        url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),
                       
]
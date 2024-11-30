
from django.urls import path , include
from . import views
from . import api


app_name = 'Jobs'
urlpatterns = [
    path('',views.Show_job,name ='show_job_list'),
    
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.show_job_details,name='jobDetails'),
    
    ##api
    path('api/', api.job_list.as_view() ,name='jobListApi'),
    path('api/<int:id>', api.job_details.as_view() ,name='jobDetailsApi'),
]



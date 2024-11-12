
from django.urls import path , include
from . import views


app_name = 'Jobs'
urlpatterns = [
    path('',views.Show_job,name ='show_job_list'),
    
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.show_job_details,name='jobDetails'),
]



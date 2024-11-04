
from django.urls import path , include
from . import views


app_name = 'Jobs'
urlpatterns = [
    path('',views.Show_job),
    
    path('<int:id>',views.show_job_details,name='jobDetails'),
]



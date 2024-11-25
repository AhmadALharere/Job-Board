
from django.urls import path , include
from . import views


app_name = 'Jobs'
urlpatterns = [
    path('',views.contact_us,name ='contact'),
    
]




from django.urls import path , include
from . import views


app_name = 'Jobs'
urlpatterns = [
    path('signup/',views.signup,name ='sign-up'),
]



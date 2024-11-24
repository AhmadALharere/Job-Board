
from django.urls import path , include
from . import views


app_name = 'Jobs'
urlpatterns = [
    path('signup',views.signup,name ='sign-up'),
    path('profile/',views.showProfile,name ='profile'),
    path('signup/Edit',views.EditProfile,name ='Edit_profile'),
]



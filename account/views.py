from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import SignupForm,Userform,Profileform
from django.contrib.auth import	authenticate,login
from .models import profile
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    
    else:
        form = SignupForm()
        return render(request,"registration/signup.html",{'form':form})


def showProfile(request):
    myprofile = profile.objects.get(user=request.user)
    return render(request,"profile/showProfile.html",{'profile':myprofile})


def EditProfile(request):
    myprofile = profile.objects.get(user=request.user)
    if request.method=='POST':
        myuserform=Userform(request.POST,instance=request.user)
        myprofileform=Profileform(request.POST,request.FILES,instance=myprofile)
        if myuserform.is_valid() and myprofileform.is_valid():
            myuserform.save()
            savedprofile=myprofileform.save(commit=False)
            savedprofile.user=request.user
            savedprofile.save()
            return redirect(reverse('account:profile'))

    else:
        myuserform=Userform(instance=request.user)
        myprofileform=Profileform(instance=myprofile)
        return render(request,"profile/editprofile.html",{"userform":myuserform,"profileform":myprofileform})


from django.shortcuts import render
from .models import Jobs
# Create your views here.

def Show_job(request):
    list_of_jobs = Jobs.objects.all()
    context = {'Job':list_of_jobs}
    return render(request,'Jobs/show Jobs.html',context)

def show_job_details(request, id):
    jobDetail = Jobs.objects.get(id=id)
    context = {'Job':jobDetail}
    return render(request,'Jobs/show job details.html',context)


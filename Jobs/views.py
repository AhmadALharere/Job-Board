from django.shortcuts import render,redirect
from .models import Jobs
from django.core.paginator import Paginator
from .form import applyform,addJob
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import jobFelter
# Create your views here.

def Show_job(request):
    list_of_jobs = Jobs.objects.all()
    
    felteringJob = jobFelter(request.GET,queryset=list_of_jobs)
    list_of_jobs = felteringJob.qs
    
    
    paginator = Paginator(list_of_jobs,2)
    pageNumber = request.GET.get('page')
    pag_obj = paginator.get_page(pageNumber)
    return render(request,'Jobs/show Jobs.html',{'Job':pag_obj,'jobfelter':felteringJob})

def show_job_details(request, slug):
    jobDetail = Jobs.objects.get(slug=slug)
    if request.method=='POST':
        form = applyform(request.POST,request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.apply_to = jobDetail
            myform.is_replayed = False
            myform.save()
            
    else:
        form = applyform()
        pass
    
    context = {'Job':jobDetail,'form':form}
    return render(request,'Jobs/show job details.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = addJob(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:show_job_list'))
            
    else:
            form = addJob()
    return render(request,'Jobs/add_job.html',{'form':form})         
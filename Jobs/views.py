from django.shortcuts import render
from .models import Jobs
from django.core.paginator import Paginator
# Create your views here.

def Show_job(request):
    list_of_jobs = Jobs.objects.all()
    paginator = Paginator(list_of_jobs,1)
    pageNumber = request.GET.get('page')
    pag_obj = paginator.get_page(pageNumber)
    return render(request,'Jobs/show Jobs.html',{'Job':pag_obj})

def show_job_details(request, id):
    jobDetail = Jobs.objects.get(id=id)
    context = {'Job':jobDetail}
    return render(request,'Jobs/show job details.html',context)


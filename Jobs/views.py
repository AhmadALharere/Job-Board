from django.shortcuts import render
from .models import Jobs
from django.core.paginator import Paginator
from .form import applyform
# Create your views here.

def Show_job(request):
    list_of_jobs = Jobs.objects.all()
    paginator = Paginator(list_of_jobs,1)
    pageNumber = request.GET.get('page')
    pag_obj = paginator.get_page(pageNumber)
    return render(request,'Jobs/show Jobs.html',{'Job':pag_obj})

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


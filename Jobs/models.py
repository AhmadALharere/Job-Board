from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
job_types = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
)

def pickImage(instance,filename):
    fname , extention = filename.split('.')
    return "Jobs/%s.%s"%(instance.id,extention)
    


# Create your models here.
class Jobs(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(default=("New Job!"), max_length=60)
    description = models.TextField(default=(""),max_length=1000)
    #location
    job_Type = models.CharField(default=("Part Time"),max_length=15,choices=job_types)
    vacancy = models.IntegerField(default=("1"))
    salary = models.IntegerField(default=("0"))
    published_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    qualification = models.IntegerField(default=("0"))
    image = models.ImageField(upload_to=pickImage)
    
    slug = models.SlugField(null=True , blank=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Jobs,self).save(*args,**kwargs)
    
    
    def __str__(self):
        return self.title
    

        
class Category(models.Model):
    title = models.CharField(default='',max_length=50)
        
    def __str__(self):
        return self.title
    
    
class apply(models.Model):
    name = models.CharField(max_length=100,default='no name')
    email = models.EmailField(max_length=120)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/", max_length=1000)
    coverletter = models.TextField(default='',max_length=500)
    apply_to = models.ForeignKey("Jobs", verbose_name=("Apply to"), on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now=True)
    is_replayed = models.BooleanField(default=False)
    

        
    def __str__(self):
        return self.name

    
    

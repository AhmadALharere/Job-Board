from django.db import models

job_types = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
)

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(default=("New Job!"), max_length=60)
    description = models.TextField(default=(""),max_length=1000)
    #location
    job_Type = models.CharField(default=("Part Time"),max_length=15,choices=job_types)
    vacancy = models.IntegerField(default=("1"))
    salary = models.IntegerField(default=("0"))
    published_on = models.DateTimeField(auto_now=True)
    #category
    qualification = models.IntegerField(default=("0"))
    Date_Line = models.DateTimeField()
    
    def __str__(self):
        return self.title
    

        
    
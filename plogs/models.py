from django.db import models

# Create your models here.

class plog(models.Model):
    title = models.CharField(default="My Plog",max_length=50)
    discription = models.TextField(default="",max_length=1000)
    #category
    #tags
    #auther = 
    published_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title    
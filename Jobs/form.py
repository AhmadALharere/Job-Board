from django import forms
from .models import apply,Jobs

class applyform(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name','email','website','cv','coverletter']
        

class addJob(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude = ('slug','owner','Date_Line')
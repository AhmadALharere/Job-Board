from django.contrib import admin

# Register your models here.

from .models import Jobs
from .models import Category
from .models import apply

admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(apply)
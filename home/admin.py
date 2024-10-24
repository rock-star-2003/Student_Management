from django.contrib import admin
from .models import Student,Batch,Department
# Register your models here.

admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Department)
from django.contrib import admin
from firstapp.models import Stud, Stud2

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','age','email']

admin.site.register(Stud,StudentAdmin)

class Student2Admin(admin.ModelAdmin):
    list_display = ['snm','semail']

admin.site.register(Stud2,Student2Admin)
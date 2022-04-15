from csv import list_dialects
from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno', 'ename', 'esal','eaddress']
admin.site.register(Employee, EmployeeAdmin)


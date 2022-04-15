import imp
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'home.html')

def saving_details(request, id= 0):
    if id == 0:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['user_name']
            email = request.POST['email']
            password = request.POST['password']
            phone_number = request.POST['phone_number']

            student = models.Student.objects.create(first_name=first_name, last_name=last_name, user_name=user_name,email=email,password=password,phone_number=phone_number)
            student.save()
            # print(first_name, last_name, user_name)
            return redirect('insert_student')
        else:
            return HttpResponse("failed")

    

def student_list(request):
    # students = models.Student.objects.all()
    # students = models.Student.objects.filter(first_name__startswith='R')
    # students = models.Student.objects.exclude(first_name__startswith='G')
    # students = models.Student.objects.order_by('first_name')
    # students = models.Student.objects.order_by('first_name').reverse()
    # students = models.Student.objects.order_by('first_name').reverse()[:4]
    # students = models.Student.objects.values()
    # students = models.Student.objects.values('first_name')
    # students = models.Student.objects.distinct()
    # students = models.Student.objects.values_list('first_name', 'last_name', named=True)
    # students = models.Student.objects.using('default')
    # students = models.Student.objects.dates('date_column', 'year') #order ='ASC/DESC' 
    # students = models.Student.objects.dates('date_column', 'month')
    # students = models.Student.objects.datetimes('column', 'year', order='asc', tzinfo=False) if tzinfo value is none it uses current time zone
    # students = models.Student.objects.none() returns nothing
    # queryset1 = models.Student.objects.values_list('first_name', 'last_name', named=True)
    # queryset2 = models.AnotheModelName.objects.values_list('col_name', 'col_name', named=True)
    # data = queryset2.union(queryset1)
    # data = queryset2.intersection(queryset1)
    # data = queryset2.difference(queryset1)
    # students = models.Student.objects.select_related('first_name')

    ############# AND OR Operators ##############

    # students = models.Student.objects.filter(id = 6) & models.Student.objects.filter(first_name  = 'Ramya')
    # students = models.Student.objects.filter( Q(id = 6 ) & Q(first_name = 'Ramya'))
    # students = models.Student.objects.filter(id = 6) | models.Student.objects.filter(first_name  = 'Ramya')


    students = models.Student.objects.all()


    return render(request, 'student_list.html', {'students':students})

def student_update(request, id):
    student = models.Student.objects.get(pk = id)
    return render(request, 'edit.html', {'student':student})

def student_updation_process(request, id):
    student = models.Student.objects.get(pk= id)
    student.delete()

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user_name = request.POST['user_name']
    email = request.POST['email']
    password = request.POST['password']
    phone_number = request.POST['phone_number']

    student = models.Student.objects.create(first_name=first_name, last_name=last_name, user_name=user_name,email=email,password=password,phone_number=phone_number)
    student.save()

    return redirect('insert_student')

def student_delete(request, id):
    student = models.Student.objects.get(pk=id)
    student.delete()
    return redirect('/student_list/')
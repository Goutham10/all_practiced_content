from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.
def date_time_view(request):
    date = datetime.now()
    hour = int(date.strftime("%H"))

    if hour < 12:
        msg = 'Hello User. good morning'
    elif hour < 16:
        msg = 'Hello User. good afternoon'
    elif hour < 21:
        msg = 'Hello User. good evening'
    else:
        msg = 'Hello User. good night'
    
    my_dict = {'date':date,'msg' : msg}

    return render(request, 'testapp/results.html', my_dict)
    
def testing1(request):
    return HttpResponse('<h3>testing</h3>')

def employee_info_view(request):
    emp_details = Employee.objects.all()
    return render(request, 'testapp/view.html', {'emp_details' : emp_details})
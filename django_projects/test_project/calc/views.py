from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name': 'Goutham'})

def add(request):
    a = int(request.POST['name1'])
    b = int(request.POST['name2'])
    res = a + b
    return render(request, 'result.html', { 'result' : res  })
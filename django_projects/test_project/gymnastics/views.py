from django.shortcuts import render

from gymnastics.models import Trainers

# Create your views here.
def index(request):
    trainers = Trainers.objects.all()
    return render(request, 'index.html',{'trainers': trainers})

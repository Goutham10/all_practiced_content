import email
from pickletools import read_uint1
from wsgiref.util import request_uri
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                                        username = user_name,
                                        password = password,
                                        email = email,
                                        first_name = first_name,
                                        last_name = last_name)
                user.save()
                print("user created ")
                return redirect('login')
        else:
            messages.info(request, 'password did not match')
            return redirect('register')
        return redirect('/')
    else:


        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings 
from authenthicating.helper import *
import uuid
#homepage
def home(request):
    return render(request, "authenthicating/home.html")
#Register feature
def Register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
        try:
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                print('Email is taken')
                return redirect('/register/')

            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                print('Username is taken')
                return redirect('/register/')

            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            return redirect('/login/')

        except Exception as e:
            print(e)

    except Exception as e:
            print(e)

    return render(request , 'authenthicating/register.html')

#Login feature
def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not username or not password:
                messages.success(request, 'Both Username and Password are required.')
                return redirect('/login/')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/login/')
            user = authenticate(username = username , password = password)
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/login/')
            # if user is trusted
            login(request , user)
            return redirect('/')  
    except Exception as e:
        print(e)
    return render(request , 'authenthicating/login.html')

#Logout feature 
def Logout(request):
    logout(request)
    return redirect('/login/') 
    # return render(request , 'authenthicating/login.html')

# forget password feature
def forgetPassPage(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            print("user existing")
            user_obj = User.objects.get(username = username)
            print("user id la" , user_obj.id)
            print("mail", user_obj.email)
            send_forget_password_mail(user_obj.email , user_obj.id)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')   
    except Exception as e:
        print(e)
    print("end function")
    return render(request,'authenthicating/forgetPassword.html')


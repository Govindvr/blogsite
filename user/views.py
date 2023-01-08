from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import user
from .models import Userdetails
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login_url')
    
    else:
        form=UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})

 
def profileView(request):
    if request.user.is_authenticated:
        username=request.user.username
        curruser = Userdetails.objects.get(user=request.user)
        return render(request,'profile.html',{'curruser':curruser})

    else:
        return redirect('login_url')

def dataView(request):
    usernm=request.user.username
    name=request.POST['name']
    description=request.POST['description'] 
    mail=request.POST['mail']
    location=request.POST['location']

    new_user=Userdetails(user=user,name=name,description=description,mail=mail,location=location)
    new_user.save()

    return render(request,'dashboard.html')

def updateView(request):
    return render(request,'data.html')
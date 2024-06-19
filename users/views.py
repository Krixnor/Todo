from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from . forms import UserRegForm, UserLogForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('signup') 
    return render(request, 'dashboard/task.html')


def sign(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists. Please choose another email.')
                return render(request, 'account/signup.html',{
        'form':form
    })
            else:
                form.save()
                return redirect('login') 

    else:
        form = UserRegForm()
    return render(request, 'account/signup.html',{
        'form':form
    })
    pass

def log(request):
    form = UserLogForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task-list') 
            # return render(request, 'dashboard/task.html')
        else:
            # messages.error(request, 'Invalid credentails')
            return render(request, 'account/login.html', {
                'message': "Invalid Credentials.",
                'form': form
            })
    return render(request, 'account/login.html',{
        'form':form
    })
    pass

def logout_view(request):
    pass


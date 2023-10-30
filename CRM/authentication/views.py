from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
                )
                user.save()
                login(request, user)
                return render(request, 'home.html')
            except:
                return HttpResponse("User already exists!")

        else: 
            return HttpResponse("Password do not match")

    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def signin(request):

    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User or pass incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'signin.html', {
        'form': AuthenticationForm
    })

def signout(request):
    logout(request)
    return redirect('signin')

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def stats(request):
    return HttpResponse("Users stats")

def main(request):
    return HttpResponse("main site")

@ensure_csrf_cookie
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            return redirect('register_success')
    else:
        form = UserCreationForm()

    return render(request, 'create_user.html', {'form': form})

def register_success(request):
    return HttpResponse("Account created successfully")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def login_success(request):
    return HttpResponse("you successfully logged in")
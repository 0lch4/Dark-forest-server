from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Stats
from django.core import serializers
from django.http import JsonResponse
    
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

@ensure_csrf_cookie
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

@csrf_exempt
def modify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        best_score = request.POST.get('best_score')

        stat, created = Stats.objects.get_or_create(username=username)
        username = User.objects.get(username=username)
        stat.update(best_score=best_score)

        return HttpResponse("Success")
    else:
        return HttpResponse("modify stats")
    
@csrf_exempt
def show(request):
    if request.method == 'GET':
        all_stats = Stats.objects.all()
        serialized_stats = serializers.serialize('json', all_stats)

        return JsonResponse(serialized_stats, safe=False)
    else:
        return HttpResponse("show stats")
    
def stats(request):
    return HttpResponse("Users stats")

def main(request):
    return HttpResponse("main site")
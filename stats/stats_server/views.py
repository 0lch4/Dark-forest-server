from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Best_score
from .models import Stats
from django.core import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
    
#creating user    
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return redirect('register_fail')
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            return redirect('register_success')
        else:
            form = UserCreationForm()
    else:
        return Response({'error': 'Invalid request.'}, status=400)

def register_success(request):
    return HttpResponse("Account created successfully")

def register_fail(request):
    return HttpResponse("Account creation failed")

# Logs the user
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return redirect('login_fail')
    else:
        return Response({'error': 'Invalid request method.'}, status=400)

def login_success(request):
    return HttpResponse("You successfully logged in")

def login_fail(request):
    return HttpResponse("You are not logged in")

#update user best score
@csrf_exempt
def modify_best_score(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        best_score = request.POST.get('best_score')

        stat, created = Best_score.objects.get_or_create(username=username)
        username = User.objects.get(username=username)
        stat.update(best_score=best_score)

        return HttpResponse("Success")
    else:
        return HttpResponse("modify stats")
    
#show users global best scores    
@csrf_exempt
def show_best_score(request):
    if request.method == 'GET':
        all_best_scores = Best_score.objects.all()
        serialized_stats = serializers.serialize('json', all_best_scores)

        return JsonResponse(serialized_stats, safe=False)
    else:
        return HttpResponse("show stats")
    
#modify users global stats
@csrf_exempt
def modify_stats(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        all_levels = request.POST.get('all_levels')
        all_gold = request.POST.get('all_gold')
        enemies_killed = request.POST.get('enemies_killed')
        destroyed_obstacles = request.POST.get('destroyed_obstacles')
        bosses_killed = request.POST.get('bosses_killed')
        devils_killed = request.POST.get('devils_killed')
        fasts_killed = request.POST.get('fasts_killed')
        mutants_killed = request.POST.get('mutants_killed')
        ghosts_killed = request.POST.get('ghosts_killed')

        stat, created = Stats.objects.get_or_create(username=username)
        username = User.objects.get(username=username)
        stat.update(all_levels=all_levels,
                    all_gold=all_gold,
                    enemies_killed=enemies_killed,
                    destroyed_obstacles=destroyed_obstacles,
                    bosses_killed=bosses_killed,
                    devils_killed=devils_killed,
                    fasts_killed=fasts_killed,
                    mutants_killed=mutants_killed,
                    ghosts_killed=ghosts_killed,
                    )
        
        return HttpResponse("Success")
    else:
        return HttpResponse("modify stats")

#show users global stats 
@csrf_exempt
def show_stats(request):
    if request.method == 'GET':
        all_stats = Stats.objects.all()
        serialized_stats = serializers.serialize('json', all_stats)

        return JsonResponse(serialized_stats, safe=False)
    else:
        return HttpResponse("show stats")
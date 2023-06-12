from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import BestScore
from .models import Stats
from django.core import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from typing import Any


# creating user
@api_view(["POST"])
def create_user(
    request: Any,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | Response | None:
    if request.method != "POST":
        return Response({"error": "Invalid request method."}, status=400)

    username = request.data.get("username")
    password = request.data.get("password")
    if User.objects.filter(username=username).exists():
        return redirect("register_fail")

    user = User.objects.create_user(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid request."}, status=400)

    UserCreationForm()
    return redirect("register_success")


@api_view(["GET"])
def register_success(request: Response) -> HttpResponse:  # noqa: ARG001
    return HttpResponse("Account created successfully")


@api_view(["GET"])
def register_fail(request: Response) -> HttpResponse:  # noqa: ARG001
    return HttpResponse("Account creation failed")


# Logs the user
@api_view(["POST"])
def login_view(
    request: Any,
) -> Response | HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.method != "POST":
        return Response({"error": "Invalid request method."}, status=400)

    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is None:
        return redirect("login_fail")

    login(request, user)
    return redirect("login_success")


@api_view(["GET"])
@login_required
def login_success(request: Response) -> HttpResponse:  # noqa: ARG001
    return HttpResponse("You successfully logged in")


@api_view(["GET"])
def login_fail(request: Response) -> HttpResponse:  # noqa: ARG001
    return HttpResponse("You are not logged in")


# update user best score
@api_view(["POST"])
@login_required
@permission_classes([IsAuthenticated])
def modify_best_score(request: Any) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        best_score = request.POST.get("best_score")

        stat, created = BestScore.objects.get_or_create(username=username)
        username = User.objects.get(username=username)
        stat.update(best_score=best_score)

        return HttpResponse("Success")
    return HttpResponse("modify stats")


# show users global best scores
@api_view(["GET"])
@login_required
def show_best_score(request: Any) -> JsonResponse | HttpResponse:
    if request.method == "GET":
        all_best_scores = BestScore.objects.all()
        serialized_stats = serializers.serialize("json", all_best_scores)

        return JsonResponse(serialized_stats, safe=False)
    return HttpResponse("show stats")


# modify users global stats
@api_view(["POST"])
@login_required
@permission_classes([IsAuthenticated])
def modify_stats(request: Any) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        all_levels = request.POST.get("all_levels")
        all_gold = request.POST.get("all_gold")
        enemies_killed = request.POST.get("enemies_killed")
        destroyed_obstacles = request.POST.get("destroyed_obstacles")
        bosses_killed = request.POST.get("bosses_killed")
        devils_killed = request.POST.get("devils_killed")
        fasts_killed = request.POST.get("fasts_killed")
        mutants_killed = request.POST.get("mutants_killed")
        ghosts_killed = request.POST.get("ghosts_killed")

        stat, created = Stats.objects.get_or_create(username=username)
        username = User.objects.get(username=username)
        stat.update(
            all_levels=all_levels,
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
    return HttpResponse("modify stats")


# show users global stats
@api_view(["GET"])
@login_required
def show_stats(request: Any) -> JsonResponse | HttpResponse:
    if request.method == "GET":
        all_stats = Stats.objects.all()
        serialized_stats = serializers.serialize("json", all_stats)

        return JsonResponse(serialized_stats, safe=False)
    return HttpResponse("show stats")

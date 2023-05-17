from django.urls import path

from . import views

urlpatterns = [
    path("stats", views.stats, name="stats"),
    path("main", views.main, name="main"),
    path('create_user', views.create_user, name='create_user'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('stats', views.stats, name='stats'),
    path('main', views.main, name='main'),
    path('create_user', views.create_user, name='create_user'),
    path('register_success', views.register_success, name='register_success'),
    path('login', views.login_view, name='login'),
    path('login_success', views.login_success, name='login_success'),
    path('modify', views.modify, name='modify'),
    path('show', views.show, name='show'),
    
]
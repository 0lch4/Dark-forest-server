from django.urls import path

from . import views
#links
urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('register_success', views.register_success, name='register_success'),
    path('register_fail', views.register_fail, name='register_fail'),
    path('login', views.login_view, name='login'),
    path('login_success', views.login_success, name='login_success'),
    path('login_fail', views.login_fail, name='login_fail'),
    path('modify_best_score', views.modify_best_score, name='modify_best_score'),
    path('show_best_score', views.show_best_score, name='show_best_score'),
    path('modify_stats', views.modify_stats, name='modify_stats'),
    path('show_stats', views.show_stats, name='show_stats'),
    
]
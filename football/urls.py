from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name="login"),
    path('',views.home, name="index"),
    path('stats/', views.stats, name='stats'),
    path('stats/?league=<league>', views.stats, name='stats_with_league'),
    path('teams/', views.teams, name='teams'),
    path('blog/', views.blog, name='blog'),
    path('banter/', views.banter, name='banter'),
    path('logout',views.logout, name="logout")
]
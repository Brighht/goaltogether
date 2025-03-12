from django.shortcuts import render
from django.contrib.auth.models import User
from .import api_call
import time

# Create your views here.
def login(request):
    return render(request, 'football/login.html')
def home(request):
    league_id = "PD"
    laliga_standing = api_call.get_standings(2014, 2024)
    time.sleep(2)
    epl_standing = api_call.get_standings(2021, 2024)
    return render(request, 'football/index.html', {
        'la_liga_standing': laliga_standing,
        'epl_standing': epl_standing
    })  

def stats(request):
    return render(request, 'football/stats.html')

def teams(request):
    return render(request, 'football/teams.html')

def blog(request):
    return render(request, 'football/blog.html')

def banter(request):
    return render(request, 'football/banter.html')
def logout(request):
    return render(request, 'football/logout.html')

#algo for adding new user
# def add_new_user(new_username):
#     users = {}
#     existing_users = {}
#     for user in new_username:
#         if user in users:
#             users[user] #return error notifying the existence of this user
#         users[user] = new_username

#track same first names 
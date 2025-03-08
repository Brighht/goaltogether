from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'football/index.html')

def stats(request):
    return render(request, 'football/stats.html')

#algo for adding new user
# def add_new_user(new_username):
#     users = {}
#     existing_users = {}
#     for user in new_username:
#         if user in users:
#             users[user] #return error notifying the existence of this user
#         users[user] = new_username

#track same first names 
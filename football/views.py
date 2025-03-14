from django.shortcuts import render
from django.contrib.auth.models import User
from .import api_call


# Create your views here.
def login(request):
    return render(request, 'football/login.html')
def home(request):
    laliga_standing = api_call.get_standings(2014, 2024)
    epl_standing = api_call.get_standings(2021, 2024)
    bundesliga_standing = api_call.get_standings(2002, 2024)
    serie_a_standing = api_call.get_standings(2019, 2024)
    return render(request, 'football/index.html', {
        'laliga_standing': laliga_standing,
        'epl_standing': epl_standing,
        'bundesliga_standing': bundesliga_standing,
        'serie_a_standing':serie_a_standing
    })  

def stats(request):
    laliga_scorers = api_call.fetch_scorers(2014, 2024)
    epl_scorers = api_call.fetch_scorers(2021,2024)
    bundeliga_scorers = api_call.fetch_scorers(2002,2024)
    serie_a_scorers = api_call.fetch_scorers(2019,2024)

    return render(request, 'football/stats.html',
                  {'laliga_scorers': laliga_scorers,
                  'epl_scorers': epl_scorers,
                  'bundesliga_scorers': bundeliga_scorers,
                  'serie_a_scorers': serie_a_scorers,
                  'selected_league': request.GET.get('league', 'Serie A')})


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
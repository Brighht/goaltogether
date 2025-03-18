import requests
from django.conf import settings

def get_standings(league_id, season):
    """
    Fetch current league standings from Football-API.
    Args:
        league_id (int): ID of the league (e.g., ## for Premier League).
    Returns:
        list: Standings data (team, rank, points) or None if failed.
    league codes for top 5 leagues
    spain
    id": 2014,
      "area": {
        "id": 2224,
        "name": "Spain",
        "code": "ESP",
        "flag": "https://crests.football-data.org/760.svg"
    portugal 
    "id": 2017,
      "area": {
        "id": 2187,
        "name": "Portugal",
        "code": "POR",
        "flag": "https://crests.football-data.org/765.svg"
      },
    Serie A(italy)
      {
      "id": 2019,
      "area": {
        "id": 2114,
        "name": "Italy",
        "code": "ITA",
        "flag": "https://crests.football-data.org/784.svg"
    },
    {
      "id": 2002,
      "area": {
        "id": 2088,
        "name": "Germany",
        "code": "DEU",
        "flag": "https://crests.football-data.org/759.svg"
      },
      "name": "Bundesliga",
      "code": "BL1",
      "type": "LEAGUE",
      "emblem": "https://crests.football-data.org/BL1.png",
      "plan": "TIER_ONE",
      "currentSeason": {
        "id": 2308,
        "startDate": "2024-08-23",
        "endDate": "2025-05-17",
        "currentMatchday": 25,
        "winner": null
      },
      "numberOfAvailableSeasons": 62,
      "lastUpdated": "2024-09-13T16:48:00Z"
    },
    {
      "id": 2021,
      "area": {
        "id": 2072,
        "name": "England",
        "code": "ENG",
        "flag": "https://crests.football-data.org/770.svg"
      },
      "name": "Premier League",
      "code": "PL",
      "type": "LEAGUE",
      "emblem": "https://crests.football-data.org/PL.png",
      "plan": "TIER_ONE",
      "currentSeason": {
        "id": 2287,
        "startDate": "2024-08-16",
        "endDate": "2025-05-25",
        "currentMatchday": 28,
        "winner": null
      },
      "numberOfAvailableSeasons": 126,
      "lastUpdated": "2024-09-13T16:51:24Z"
    },

    """
    url = f'http://api.football-data.org/v4/competitions/{league_id}/standings?season={season}' #
    api_key = settings.FOOTBALL_DATA_KEY
    headers = {'X-Auth-Token': api_key}
    
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status() 
        
        api_response = response.json()
        league_standing = api_response['standings'][0]['table']
      
        return league_standing
    
    except requests.RequestException as e:
        print(f"Error fetching standings for league {league_id}: {e}")
        return []
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error parsing standings for league {league_id}: {e}")
        return []

def fetch_scorers(league_id, season):
    url = f'http://api.football-data.org/v4/competitions/{league_id}/scorers'
    headers = {'X-Auth-Token': settings.FOOTBALL_DATA_KEY}
    
    try:
        response = requests.get(url=url, headers=headers, params={'season': season})
        response.raise_for_status()
        
        scorer_data = response.json()
        if 'scorers' in scorer_data:
            scorers_arr = scorer_data['scorers']
        else:
            scorers_arr = []
        
        print(f"Status: {response.status_code} - Scorers for {league_id}: {scorers_arr}")
        return scorers_arr

    except requests.RequestException as e:
        print(f"Error fetching scorers for league {league_id}: {e}")
        return []
# def stats(selected_league):
#     context = {'selected_league' : selected_league,
#                'laliga' : api}
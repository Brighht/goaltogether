import requests
from django.conf import settings

def get_standings(league_id):
    """
    Fetch current league standings from Football-API.
    Args:
        league_id (int): ID of the league (e.g., ## for Premier League).
    Returns:
        list: Standings data (team, rank, points) or None if failed.
    """
    url = f'http://api.football-data.org/v4/competitions/{league_id}/standings'
    api_key = settings.FOOTBALL_DATA_KEY
    headers = { 'X-Auth-Token': api_key }
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        print("Successful fetch")
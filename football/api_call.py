import requests
from django.conf import settings

def get_standings(league_id):
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

    """
    url = f'http://api.football-data.org/v4/competitions/{league_id}/standings'
    api_key = settings.FOOTBALL_DATA_KEY
    headers = { 'X-Auth-Token': api_key }
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        try:
            api_response = response.json()
            league_standing = api_response["standings"][0]["table"]

        except requests.RequestException as e:
            print(f"Error fetching stadings {e}")
    return league_standing
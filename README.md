
---

# Goaltogether

A fun football web app for me and my friends to track our games, share updates, and have a laugh. Built with Python and Django, it’s ready to grow big—think league standings, live matches, and even machine learning predictions down the road.

## What It Does (Right Now)
- Log goals from our pickup games.
- Post messages like “Match at 5 PM!”
- Show a leaderboard of top scorers.
- Football vibe—green, bold, simple.

## Future Goals
- Add league standings, team lists, and live match updates.
- Plug in machine learning to predict scorers or analyze stats.

## Setup
1. **Requirements**  
   - Python 3.9+  
   - Django (install with `pip install django`)  

2. **Get It Running**  
   - Clone this repo: `git clone [https://github.com/Brighht/goaltogether.git]`  
   - Go to the folder: `cd goaltogether`  
   - Start the football app: `python manage.py startapp football`  
   - Add `'football'` to `INSTALLED_APPS` in `goaltogether/settings.py`  
   - Create the database: `python manage.py migrate`  
   - Run it: `python manage.py runserver`  
   - Visit: `localhost:8000`  

3. **Add Yourself**  
   - Make a superuser: `python manage.py createsuperuser`  
   - Log in at `/admin` to add players or goals.

## Structure
- **`goaltogether`**: The main project—runs the show.  
- **`football`**: The app—handles all football stuff (goals, messages, standings, etc.).  
- **`more-to-come`** 

## Why It’s Cool
- Built for us to enjoy football together.  
- Easy to share locally (Wi-Fi for now).  
- Set up for big ideas—ML-ready with clean data.

## To-Do
- Add forms for goals/messages.  
- Style it like a pitch.  
- Expand to live matches and stats.

---

## Progress
- Building
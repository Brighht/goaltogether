from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
__________________________________________________________________
|<profile_photo>user_bright: Drinking the tears of the opponent  |
|created_at : 3/5/2025 - 11:09AM                                 |
|<likes-button><23>                                              |
|  |<profile_photo>user_goalz: Salty but delicious!              |
|  |created_at : 3/5/2025 - 11:12AM                              |
|  |<likes-button><5>                                            |
|________________________________________________________________|
From: Responses model.
Fields:
message = ForeignKey(Messages) → Links to "user_bright’s" post.
sender = ForeignKey(User) → "user_goalz".
response_text = CharField(max_length=1000) → "Salty but delicious!".
created_at = DateTimeField(auto_now_add=True) → "3/5/2025 - 11:12AM".
(likes not yet added—could add IntegerField here too).
'''

class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_jersey_number = models.IntegerField()
    player_nationality = models.CharField(max_length=100)
    player_age = models.IntegerField()
    team_name  = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    date_joined = models.DateField()

class Teams(models.Model):
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField
    team_est = models.DateField() #enter date manually
    team_stadium_name = models.CharField(max_length=100)
    
class Messages(models.Model):
    #add logged in user's name to it
    message_text = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
class Responses(models.Model):
    messages = models.ForeignKey(Messages)
    sender = models.ForeignKey(User)
    response_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
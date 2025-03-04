from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    
    
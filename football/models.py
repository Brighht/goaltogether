from django.db import models

# Create your models here.
class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_jersey_number = models.IntegerField()
    player_nationality = models.CharField(max_length=100)
    player_age = models.IntegerField()
    team_name  = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    date_joined = models.DateField()
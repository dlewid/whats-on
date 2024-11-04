
from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    sport_category = models.CharField(max_length=200)
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    date = models.DateTimeField()
    time = models.DateTimeField(default=timezone.now)


from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    sport_category = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

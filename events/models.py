
from django.db import models
from django.utils import timezone
from django.db import models


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)  # This is your primary key
    home_team = models.CharField(max_length=200, default="none")
    away_team = models.CharField(max_length=200, default="none")
    # This should match your DB column
    sport = models.CharField(max_length=200, default="none")
    event_date = models.DateField(default="2020-01-01")  # Date field
    event_time = models.TimeField(default="00:00")  # Time field

    class Meta:
        db_table = 'events'  # Ensures this model uses the existing events table in the DB
        managed = False


class Review(models.Model):  # The Review model
    review_text = models.CharField(max_length=200)
    stars = models.IntegerField(default=0)

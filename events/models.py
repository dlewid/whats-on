
from django.db import models
from django.utils import timezone
from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)  # This is your primary key
    home_team = models.CharField(max_length=200, default="none")
    away_team = models.CharField(max_length=200, default="none")
    sport = models.CharField(max_length=200, default="none")  # This should match your DB column
    event_date = models.DateField(default="2020-01-01")  # Date field
    event_time = models.TimeField(default="00:00")  # Time field

    class Meta:
        db_table = 'events'  # Ensures this model uses the existing events table in the DB
        managed = False

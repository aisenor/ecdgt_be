from django.db import models

from backend.models.division import Division
from backend.models.player import Player
from backend.models.event import Event


class EventResults(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    event_rank = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'event_results'

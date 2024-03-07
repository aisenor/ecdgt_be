from django.db import models

from backend.models.division import Division
from backend.models.player import Player


class Standings(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    points = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        db_table = 'standings'

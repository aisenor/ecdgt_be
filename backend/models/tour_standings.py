from django.db import models


class TourStandings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    points = models.IntegerField()
    division = models.CharField(max_length=255)
    pdga_number = models.IntegerField()
    event = models.CharField(max_length=255)

    class Meta:
        db_table = 'tour_standings'

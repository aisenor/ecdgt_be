from django.db import models


class TourDates(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False, blank=False)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, unique=True)
    province = models.CharField(max_length=255)

    class Meta:
        db_table = 'tour_dates'

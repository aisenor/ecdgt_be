from backend.models.event_type import EventType

from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    text = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'event'

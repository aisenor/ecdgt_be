from django.db import models


class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'event_type'

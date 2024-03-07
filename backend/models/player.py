from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pdga_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'player'

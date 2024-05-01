# backend/admin.py

from django.contrib import admin
from .models.player import Player
from .models.event import Event
from .models.division import Division
from .models.event_results import EventResults

admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Division)
admin.site.register(EventResults)

from rest_framework import serializers

from backend.models.event_results import EventResults


class EventResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventResults
        fields = (
            "id",
            "player",
            "event",
            "event_rank",
            "division"
        )

from rest_framework import serializers

from backend.models.event import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "date",
            "text",
            "province",
            "course",
            "link",
        )

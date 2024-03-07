from rest_framework import serializers

from backend.models.standings import Standings


class StandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standings
        fields = (
            "id",
            "player",
            "points",
            "rank",
            "division"
        )

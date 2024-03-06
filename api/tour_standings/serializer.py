from rest_framework import serializers

from backend.models.tour_standings import TourStandings


class TourStandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourStandings
        fields = (
            "id",
            "name",
            "points",
            "division",
            "pdga_number",
            "event"
        )

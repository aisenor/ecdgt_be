from rest_framework import serializers

from backend.models.tour_dates import TourDates


class TourDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDates
        fields = (
            "id",
            "date",
            "name",
            "link",
            "province"
        )

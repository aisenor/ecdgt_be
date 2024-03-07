from rest_framework import serializers

from backend.models.player import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            "id",
            "name",
            "pdga_number"
        )

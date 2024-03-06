from rest_framework import serializers

from backend.models.division import Division


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = (
            "id",
            "name"
        )

from django_filters import rest_framework as filters

from backend.models.player import Player


class PlayerFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='exact')
    pdga_number = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Player
        fields = ['name', 'pdga_number']

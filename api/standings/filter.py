from django_filters import rest_framework as filters

from backend.models.standings import Standings


class StandingsFilter(filters.FilterSet):
    player = filters.NumberFilter(lookup_expr='exact')
    division = filters.NumberFilter(lookup_expr='exact')
    points = filters.NumberFilter(lookup_expr='exact')
    rank = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Standings
        fields = ['player', 'division', 'points', 'rank']

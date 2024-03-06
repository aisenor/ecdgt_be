from django_filters import rest_framework as filters

from backend.models.tour_standings import TourStandings


class TourStandingsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='exact')
    points = filters.NumberFilter(lookup_expr='exact')
    division = filters.CharFilter(lookup_expr='exact')
    pdga_number = filters.CharFilter(lookup_expr='exact')
    event = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = TourStandings
        fields = ['name', 'points', 'division', 'pdga_number', 'event']

from django_filters import rest_framework as filters

from backend.models.event_results import EventResults


class EventResultsFilter(filters.FilterSet):
    player = filters.CharFilter(lookup_expr='exact')
    event = filters.NumberFilter(lookup_expr='exact')
    event_rank = filters.NumberFilter(lookup_expr='exact')
    division = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = EventResults
        fields = ["player", "event", "event_rank", "division"]

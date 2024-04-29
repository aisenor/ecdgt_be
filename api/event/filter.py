from django_filters import rest_framework as filters

from backend.models.event import Event


class EventFilter(filters.FilterSet):
    date = filters.CharFilter(lookup_expr='exact')
    text = filters.CharFilter(lookup_expr='contains')
    province = filters.CharFilter(lookup_expr='contains')
    course = filters.CharFilter(lookup_expr='contains')
    link = filters.CharFilter(lookup_expr='exact')
    event_type = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['date', 'text', 'province', 'course', 'link', 'event_type']

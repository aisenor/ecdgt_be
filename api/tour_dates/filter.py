from django_filters import rest_framework as filters

from backend.models.tour_dates import TourDates


class TourDatesFilter(filters.FilterSet):
    date = filters.CharFilter(lookup_expr='exact')
    name = filters.CharFilter(lookup_expr='contains')
    link = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = TourDates
        fields = ['date', 'name', 'link']

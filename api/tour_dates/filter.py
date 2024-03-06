from django_filters import rest_framework as filters

from backend.models.tour_dates import TourDates


class TourDatesFilter(filters.FilterSet):
    date = filters.CharFilter(lookup_expr='exact')
    name = filters.CharFilter(lookup_expr='contains')
    link = filters.CharFilter(lookup_expr='exact')
    province = filters.CharFilter(lookup_expr='contains')
    course = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TourDates
        fields = ['date', 'name', 'link', 'province', 'course']

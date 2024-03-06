from django_filters import rest_framework as filters

from backend.models.division import Division


class DivisionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Division
        fields = ['name']

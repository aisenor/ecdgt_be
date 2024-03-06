from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import TourStandingsSerializer
from .filter import TourStandingsFilter
from backend.models.tour_standings import TourStandings

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
        ]
    )
)
class TourStandingsListView(ListCreateAPIView):
    serializer_class = TourStandingsSerializer
    queryset = TourStandings.objects.all()
    filterset_class = TourStandingsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'tour_standings': serializer.data})

        return Response({'tour_standings': serializer.data})

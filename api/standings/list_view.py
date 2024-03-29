from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import StandingsSerializer
from .filter import StandingsFilter
from backend.models.standings import Standings

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
        ]
    )
)
class StandingsListView(ListCreateAPIView):
    serializer_class = StandingsSerializer
    queryset = Standings.objects.all()
    filterset_class = StandingsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'standings': serializer.data})

        return Response({'standings': serializer.data})

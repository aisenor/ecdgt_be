from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .serializer import TourStandingsSerializer
from backend.models.tour_standings import TourStandings

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Retrieve",
        operation_description=""
    )
)
class TourStandingsDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "post"]
    serializer_class = TourStandingsSerializer
    queryset = TourStandings.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print({'tour_standings': serializer.data})
        return Response({'tour_standings': serializer.data})

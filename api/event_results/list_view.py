from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import EventResultsSerializer
from .filter import EventResultsFilter
from backend.models.event_results import EventResults

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
        ]
    )
)
class EventResultsListView(ListCreateAPIView):
    serializer_class = EventResultsSerializer
    queryset = EventResults.objects.all()
    filterset_class = EventResultsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'event_results': serializer.data})

        return Response({'event_results': serializer.data})

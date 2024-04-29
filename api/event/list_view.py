from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import EventSerializer
from .filter import EventFilter
from backend.models.event import Event

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
            openapi.Parameter(
                name="date",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False
            ),
            openapi.Parameter(
                name="text",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name="link",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name="province",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['NS', 'NS', 'PEI', 'NFL'],
                required=False
            ),
            openapi.Parameter(
                name="course",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name="event_type",
                description="Event number of days",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=[1, 2],
                required=False
            ),
        ]
    )
)
class EventListView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_class = EventFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'event': serializer.data})

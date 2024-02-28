from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import TourDatesSerializer
from .filter import TourDatesFilter
from backend.models.tour_dates import TourDates

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
                name="name",
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
        ]
    )
)
class TourDatesListView(ListCreateAPIView):
    serializer_class = TourDatesSerializer
    queryset = TourDates.objects.all()
    filterset_class = TourDatesFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'TourDates': serializer.data})
        return Response({'TourDates': serializer.data})

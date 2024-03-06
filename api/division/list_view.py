from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import DivisionSerializer
from .filter import DivisionFilter
from backend.models.division import Division

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
        ]
    )
)
class DivisionListView(ListCreateAPIView):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()
    filterset_class = DivisionFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'divisions': serializer.data})

        return Response({'division': serializer.data})

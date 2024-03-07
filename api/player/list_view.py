from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import PlayerSerializer
from .filter import PlayerFilter
from backend.models.player import Player

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
        ]
    )
)
class PlayerListView(ListCreateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    filterset_class = PlayerFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print({'player': serializer.data})

        return Response({'player': serializer.data})

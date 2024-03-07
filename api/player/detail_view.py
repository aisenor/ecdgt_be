from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .serializer import PlayerSerializer
from backend.models.player import Player

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Retrieve",
        operation_description=""
    )
)
class PlayerDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "post"]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print({'player': serializer.data})
        return Response({'player': serializer.data})

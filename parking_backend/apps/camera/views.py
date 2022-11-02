from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from parking_backend.apps.camera.models import Camera
from parking_backend.apps.camera.serializers import CameraSerializer


# Create your views here.
class CameraListCreateAPIView(ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'id',
        'parking_place__id',
        'parking_place__user',
        'code',
        'name',
        'ip_cam'
    ]

    def get_queryset(self):
        return self.queryset.filter(parking_place__user=self.request.user)


class CameraRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

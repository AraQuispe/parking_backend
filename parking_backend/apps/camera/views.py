from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from parking_backend.apps.camera.models import Camera
from parking_backend.apps.camera.serializers import CameraSerializer

from django.views.decorators import gzip
from parking_backend.apps.camera.Code import VideoCamara as vc
from django.http import StreamingHttpResponse
from django.shortcuts import render


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


@gzip.gzip_page
def ipCamara(request):
    # return render(request,'Camara/index.html')
    ###########################################
    try:
        cam = vc.VideoCamara()
        return StreamingHttpResponse(vc.gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    #return render(request, 'index.html')
    ###########################################

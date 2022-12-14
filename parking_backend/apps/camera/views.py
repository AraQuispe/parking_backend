import threading

from django.http import StreamingHttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from parking_backend.apps.camera.core.compressing_streaming import compressing_streaming
from parking_backend.apps.camera.core.video_camera import VideoCamera
from parking_backend.apps.camera.core.video_processing import video_processing
from parking_backend.apps.camera.models import Camera
from parking_backend.apps.camera.serializers import CameraSerializer


# Create your views here.
from parking_backend.apps.parking_place.models import ParkingPlace


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


class CameraStreamingAPIView(APIView):
    def get(self, request):
        seconds = int(self.request.query_params.get('seconds', 4))
        url_camera = self.request.query_params.get('url_camera', 0)
        try:
            cam = VideoCamera(url_camera)
            return StreamingHttpResponse(
                compressing_streaming(cam, seconds),
                content_type="multipart/x-mixed-replace;boundary=frame"
            )
        except:
            pass


class CameraProcessingRunningAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            cameras = Camera.objects.filter(parking_place__user=2)
            parking = ParkingPlace.objects.get(user=2)
        else:
            cameras = Camera.objects.filter(parking_place__user=request.user)
            parking = ParkingPlace.objects.get(user=2)

        for camera in cameras:
            if camera.active:
                if camera.ip_cam == "0.0.0.0":
                    capture_camera = VideoCamera(0)
                else:
                    capture_camera = VideoCamera(camera.ip_cam)
                threading.Thread(
                    target=self.processing_video_streaming_thread,
                    args=[camera, capture_camera]
                ).start()
        threading.Thread(
            target=self.set_available_places_parking_thread,
            args=[cameras, parking]
        ).start()
        return "Thread Inicializado"

    @staticmethod
    def processing_video_streaming_thread(camera_data, capture_camera):
        while True:
            nro_plazas = video_processing(capture_camera.frame)
            # Actualizar
            camera_data.places = nro_plazas
            camera_data.save()

    @staticmethod
    def set_available_places_parking_thread(cameras_data, parking):
        while True:
            nro_plazas = 0
            for camera in cameras_data:
                nro_plazas += camera.places
            parking.available = nro_plazas
            parking.save()
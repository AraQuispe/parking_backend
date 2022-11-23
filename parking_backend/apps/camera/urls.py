from django.urls import path

from parking_backend.apps.camera.views import CameraListCreateAPIView, CameraRetrieveUpdateDestroyAPIView, \
    CameraStreamingAPIView, CameraProcessingRunningAPIView

urlpatterns = [
    path('', CameraListCreateAPIView.as_view()),
    path('<int:pk>', CameraRetrieveUpdateDestroyAPIView.as_view()),
    path('stream-camera/', CameraStreamingAPIView.as_view()),
    path('monitoring-demon/', CameraProcessingRunningAPIView.as_view())
]

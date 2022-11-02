from django.urls import path

from parking_backend.apps.camera.views import CameraListCreateAPIView, CameraRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CameraListCreateAPIView.as_view()),
    path('<int:pk>', CameraRetrieveUpdateDestroyAPIView.as_view()),
]

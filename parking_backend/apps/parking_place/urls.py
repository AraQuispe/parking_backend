from django.urls import path

from parking_backend.apps.parking_place.views import ParkingPlaceRetrieveUpdateDestroyAPIView, \
    ParkingPlaceListCreateAPIView

urlpatterns = [
    path('', ParkingPlaceListCreateAPIView.as_view()),
    path('<int:pk>', ParkingPlaceRetrieveUpdateDestroyAPIView.as_view()),
]

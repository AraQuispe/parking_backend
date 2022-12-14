from django.urls import path

from parking_backend.apps.parking_place.views import ParkingPlaceRetrieveUpdateDestroyAPIView, \
    ParkingPlaceListCreateAPIView, ParkingPlaceListAPIView, ParkingPlaceRetrieveAPIView

urlpatterns = [
    path('', ParkingPlaceListCreateAPIView.as_view()),
    path('<int:pk>', ParkingPlaceRetrieveUpdateDestroyAPIView.as_view()),
    path('api/allPlaces', ParkingPlaceListAPIView.as_view()),
    path('api/<int:pk>', ParkingPlaceRetrieveAPIView.as_view())
]

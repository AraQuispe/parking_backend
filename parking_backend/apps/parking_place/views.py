from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from parking_backend.apps.parking_place.models import ParkingPlace
from parking_backend.apps.parking_place.serializers import ParkingPlaceSerializer


# Create your views here.
# Create your views here.
class ParkingPlaceListCreateAPIView(ListCreateAPIView):
    queryset = ParkingPlace.objects.all()
    serializer_class = ParkingPlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'id',
        'user',
        'name'
    ]


class ParkingPlaceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ParkingPlace.objects.all()
    serializer_class = ParkingPlaceSerializer

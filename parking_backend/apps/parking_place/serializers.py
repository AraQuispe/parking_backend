from rest_framework import serializers

from parking_backend.apps.parking_place.models import ParkingPlace


class ParkingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingPlace
        fields = '__all__'

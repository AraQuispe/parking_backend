from rest_framework import serializers

from parking_backend.apps.camera.models import Camera


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

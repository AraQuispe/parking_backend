from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from parking_backend.apps.user.models import MyUser
from parking_backend.apps.user.serializers import MyUserSerializer


# Create your views here.
class MyUserListCreateAPIView(ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user__id',
        'user__username'
    ]


class MyUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

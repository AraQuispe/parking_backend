from django.urls import path

from parking_backend.apps.user.views import MyUserRetrieveUpdateDestroyAPIView, MyUserListCreateAPIView

urlpatterns = [
    path('', MyUserListCreateAPIView.as_view()),
    path('<int:pk>', MyUserRetrieveUpdateDestroyAPIView.as_view()),
]

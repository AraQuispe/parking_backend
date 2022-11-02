from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Model

from parking_backend.apps.user.models import MyUser
from parking_backend.base_model import BaseModel


# Create your models here.
class ParkingPlace(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='parkingplace_user')
    name = models.TextField(null=False, blank=False, max_length=128)
    latitude = models.DecimalField(null=False, decimal_places=4, max_digits=8)
    longitude = models.DecimalField(null=False, decimal_places=4, max_digits=8)
    address = models.TextField(null=False, blank=False, max_length=128)
    opening_time = models.TimeField(null=False, blank=False)
    closing_time = models.TimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, max_length=256)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=8)
    max_capacity = models.IntegerField(null=False)
    available = models.IntegerField(null=False)

    def __str__(self):
        return f'{type(self).__name__}({", ".join("%s=%s" % item for item in vars(self).items() if item[0][0] != "_")})'

    class Meta:
        verbose_name = 'Zona de Parqueo'
        verbose_name_plural = 'Zonas de Parqueo'

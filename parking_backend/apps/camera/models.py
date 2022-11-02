from django.db import models
from django.db.models import Model

from parking_backend.apps.parking_place.models import ParkingPlace
from parking_backend.base_model import BaseModel


# Create your models here.
class Camera(BaseModel):
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, related_name='parkingplace_camera')
    code = models.TextField(null=False, blank=False, max_length=256)
    name = models.TextField(null=False, blank=False, max_length=128)
    ip_cam = models.TextField(null=False, blank=False, max_length=256)
    ref_location = models.TextField(null=False, blank=False, max_length=256)
    note = models.TextField(null=False, blank=True, max_length=256)
    pos_sup_x = models.IntegerField(null=True)
    pos_sup_y = models.IntegerField(null=True)
    pos_inf_x = models.IntegerField(null=True)
    pos_inf_y = models.IntegerField(null=True)
    places = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{type(self).__name__}({", ".join("%s=%s" % item for item in vars(self).items() if item[0][0] != "_")})'

    class Meta:
        verbose_name = 'Camara'
        verbose_name_plural = 'Camaras'

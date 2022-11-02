from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from parking_backend.base_model import BaseModel


# Create your models here.
class MyUser(BaseModel):
    user = models.OneToOneField(User, on_delete=CASCADE, primary_key=True)

    def __str__(self):
        return f'{type(self).__name__}({", ".join("%s=%s" % item for item in vars(self).items() if item[0][0] != "_")})'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

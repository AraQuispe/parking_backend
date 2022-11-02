import datetime

from django.db import models
from django.db.models import Model
from django.utils import timezone


class BaseModel(Model):
    is_deleted = models.BooleanField(null=False, default=False)
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(default=None)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

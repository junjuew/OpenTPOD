from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Status(Enum):
    CREATED = 'created'
    TRAINING = 'training'
    TRAINED = 'trained'

    @classmethod
    def choices(self):
        return tuple((x.value, x.name) for x in self)

    def __str__(self):
        return self.value

class Detector(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User, null=True, blank=True,
        on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=Status.choices(),
        default=Status.CREATED)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    notes = models.CharField(max_length=254)
    medication = PickledObjectField(null=True)

    def __str__(self):
        return self.name

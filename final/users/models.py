# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    straat = models.CharField(max_length=64, null=True)
    huisnummer = models.IntegerField(null=True)
    postcode = models.CharField(max_length=6, null=True)
    woonplaats = models.CharField(max_length=64, null=True)
    # add additional fields in here

    def __str__(self):
        return self.username
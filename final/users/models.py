# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    geboortedatum = models.DateField()
    straat = models.CharField(max_length=64)
    huisnummer = models.IntegerField()
    postcode = models.CharField(max_length=6)
    woonplaats = models.CharField(max_length=64)
    gebouw = models.IntegerField()
    verdieping = models.IntegerField()

    def __str__(self):
        return self.username
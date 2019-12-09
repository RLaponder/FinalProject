from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from users.models import CustomUser

class Activiteit(models.Model):
    name = models.CharField(max_length=128)
    gebruiker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datum = models.DateField()
    starttijd = models.CharField(max_length=5)
    eindtijd = models.CharField(max_length=5)
    straat = models.CharField(max_length=64)
    huisnummer = huisnummer = models.IntegerField()
    postcode = models.CharField(max_length=6)
    plaats = models.CharField(max_length=64)
    gebouw = models.IntegerField(blank=True)
    verdieping = models.IntegerField(blank=True)
    categorie = models.CharField(max_length=64)
    uitgenodigd = models.BooleanField()
    # Nog toevoegen: personen die aanwezig zijn. ManyToManyField??

    def __str__(self):
        return f"{self.name} van {self.gebruiker} op {self.datum}"
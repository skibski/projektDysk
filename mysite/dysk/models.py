from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.template import Context, Template


class Dysk(models.Model):
    id_dysku = models.IntegerField(default=0)
    rozmiar_calkowity = models.IntegerField(default=0)
    rozmiar_zajety = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dysk_name

    @property
    def calculate(self):
        return (self.rozmiar_zajety * 100)/self.rozmiar_calkowity

class Katalog(models.Model):
    id_katalogu = models.IntegerField(default=0)
    nazwa = models.CharField(max_length=200)
    id_dysku = models.ForeignKey(Dysk, on_delete=models.CASCADE)
    sciezka_do_katalogu = models.CharField(max_length=200)


class Plik(models.Model):
    id_pliku = models.IntegerField(default=0)
    nazwa = models.CharField(max_length=200)
    id_katalogu = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    typ_pliku = models.CharField(max_length=200)
    sciezka_do_pliku = models.CharField(max_length=200)

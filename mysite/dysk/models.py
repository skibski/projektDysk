from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Dysk(models.Model):
    id_dysku = models.IntegerField(default=0)
    rozmiar_calkowity = models.IntegerField(default=0)
    rozmiar_zajety = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


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

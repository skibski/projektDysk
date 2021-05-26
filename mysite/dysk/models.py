from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.template import Context, Template
from django.core.validators import FileExtensionValidator


class Dysk(models.Model):
    id_dysku = models.IntegerField(default=0)
    rozmiar_calkowity = models.IntegerField(default=0)
    rozmiar_zajety = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def calculate(self):
        return (self.rozmiar_zajety * 100)/(self.rozmiar_calkowity*1000)

class Katalog(models.Model):
    id_katalogu = models.IntegerField(default=0)
    nazwa = models.CharField(max_length=200)
    id_dysku = models.ForeignKey(Dysk, on_delete=models.CASCADE)
    sciezka_do_katalogu = models.CharField(max_length=200)
    id_katalogu_nadrzednego = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)


class Plik(models.Model):
    id_pliku = models.IntegerField(default=0)
    nazwa = models.CharField(max_length=200)
    id_katalogu = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    typ_pliku = models.CharField(max_length=200)
    sciezka_do_pliku = models.CharField(max_length=200)


class Document(models.Model):
    id_dokumentu = models.IntegerField(default=0)
    id_katalogu = models.ForeignKey(Katalog, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=255, default='Document_name')
    typ_pliku = models.CharField(max_length=200,default="*")
    sciezka_do_pliku = models.CharField(max_length=200,default="/")
    udostepnienie = models.BooleanField(default=False)
    myfile = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx', 'txt', 'jpg', 'png'])
    ])

    def __str__(self):
        return self.name

# class SharedDocument(models.Model):
#     id_dokumentu=models.ForeignKey(Document, on_delete=models.CASCADE, default=0)
#     udostepniony=models.

class Widok(models.Model):
    id_widoku = models.IntegerField(default=0)
    nazwa = models.CharField(max_length=255,default="*")
    tresc = models.TextField(default='Text sample')

class SchowekPlik(models.Model):
    id_schowka = models.IntegerField(default=0)
    id_pliku = models.ForeignKey(Document, on_delete=models.CASCADE, default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
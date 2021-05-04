from django.shortcuts import render
from .models import Dysk, Katalog, Plik
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def profile(request):
    all_objects=Dysk.objects.all()
    context={'all_objects': all_objects}
    return render(request,'pages/profile.html', context)

def disk(request, disk_id):
    disk = Dysk.objects.get(id_dysku=disk_id)
    catalogs = Katalog.objects.filter(id_dysku=disk)
    mydict = {'disk': disk, 'catalogs': catalogs}
    return render(request, 'pages/disk.html', context=mydict)

def catalog(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id_dysku=disk_id)
    catalog = Katalog.objects.get(id_katalogu=catalog_id)
    files = Plik.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files}
    return render(request, 'pages/catalog.html', context=mydict)
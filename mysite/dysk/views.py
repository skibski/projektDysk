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
    disk = Dysk.objects.get(id=disk_id)
    catalogs = Katalog.objects.filter(id_dysku=disk)
    mydict = {'disk': disk, 'catalogs': catalogs}
    return render(request, 'pages/disk.html', context=mydict)

def diskDelete(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    disk.delete()
    # profile(request)
    all_objects=Dysk.objects.all()
    context={'all_objects': all_objects}
    return render(request,'pages/profile.html', context)

def catalog(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id=catalog_id)
    files = Plik.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files}
    return render(request, 'pages/catalog.html', context=mydict)

def addStandard(request):
    # profile(request)
    all_objects = Dysk.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/profile.html', context)

def addStandard(request, user_id):
    u = User.objects.get(id=user_id)
    disk = Dysk()
    disk.rozmiar_calkowity=5
    disk.rozmiar_zajety=0
    disk.id_user=u
    disk.save()
    # profile(request)
    all_objects = Dysk.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/profile.html', context)

def addPremium(request):
    # profile(request)
    all_objects = Dysk.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/profile.html', context)

def addPremium(request, user_id):
    u = User.objects.get(id=user_id)
    disk = Dysk()
    disk.rozmiar_calkowity=10
    disk.rozmiar_zajety=0
    disk.id_user=u
    disk.save()
    # profile(request)
    all_objects = Dysk.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/profile.html', context)
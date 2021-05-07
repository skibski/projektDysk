from django.shortcuts import render
from .models import Dysk, Katalog, Plik
from django.contrib.auth.models import User
from .forms import DocumentForm
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
    root = Katalog()
    root.nazwa="root"
    root.id_dysku=disk
    root.sciezka_do_katalogu="/"
    root.save()
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
    root = Katalog()
    root.nazwa = "root"
    root.id_dysku = disk
    root.sciezka_do_katalogu = "/"
    root.save()
    return render(request, 'pages/profile.html', context)

def addCatalog(request):
    return render(request,'/pages/profile.html')

def addCatalog(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog()
    catalog.nazwa = "new_catalog"
    catalog.id_dysku = disk
    catalog.sciezka_do_katalogu="/new_catalog"
    catalog.save()
    return render(request, 'pages/profile.html', context)

def deleteCatalog(request):
    return render(request, 'pages/profile.html', context)

def deleteCatalog(request, catalog_id):
    catalog = Katalog.objects.get(id=catalog_id)
    catalog.delete()
    return render(request, 'pages/profile.html', context)

def upload(request):
    if request.user.is_authenticated:
        # Is it better to use @login_required ?
        username = request.user.username
    else:
        username = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            return render(request, 'pages/upload.html', {
               "form": DocumentForm(),
               "uploaded_file_url": doc.myfile.url,
               "username": username,
            })
    else:
        form = DocumentForm()
    return render(request, 'pages/upload.html', {"form": form})
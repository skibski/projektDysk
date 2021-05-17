from django.shortcuts import render
from .models import Dysk, Katalog, Plik, Document
from django.contrib.auth.models import User
from .forms import DocumentForm
from django.shortcuts import get_object_or_404


def about(request):
    return render(request, 'pages/about.html')

def profile(request):
    all_objects=Dysk.objects.all()
    context={'all_objects': all_objects}
    return render(request,'pages/profile.html', context)

def disk(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id_dysku=disk, nazwa="root")
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)

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
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog_id)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)

def catalogNadrzedny(request, disk_id, catalog_id, catalog_nadrzedny_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id=catalog_id)
    catalogNadrzedny = Katalog.objects.get(id=catalog_nadrzedny_id)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': catalogNadrzedny}
    return render(request, 'pages/catalog.html', context=mydict)

def addStandard(request):
    # profile(request)
    all_objects = Dysk.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/profile.html', context)

def addStandard(request, user_id):
    u = User.objects.get(id=user_id)
    disk = Dysk()
    disk.rozmiar_calkowity=1
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
    disk.rozmiar_calkowity=5
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
    all_objects = Katalog.objects.all()
    context = {'all_objects': all_objects}
    catalog = Katalog()
    catalog.nazwa = "new_catalog"
    catalog.id_dysku = disk
    catalog.sciezka_do_katalogu="/new_catalog"
    catalog.save()
    return render(request, 'pages/profile.html',context)

def addCatalogNadrzedny(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id=disk_id)
    id_katalogu=Katalog.objects.get(id=catalog_id)
    catalog = Katalog()
    catalog.nazwa = "new_catalog_nizej"
    catalog.id_dysku = disk
    catalog.sciezka_do_katalogu="/new_catalog"
    catalog.id_katalogu_nadrzednego=id_katalogu

    id_nadrzednego=catalog.id_katalogu_nadrzednego
    catalog.save()

    cat = Katalog.objects.get(id=id_nadrzednego.id)
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=id_nadrzednego.id)
    files = Document.objects.filter(id_katalogu=id_nadrzednego.id)
    mydict = {'disk': disk, 'catalog': cat, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)

# def deleteCatalog(request):
#     return render(request, 'pages/profile.html', context)

def deleteCatalog(request, catalog_id):

    catalog = Katalog.objects.get(id=catalog_id)
    disk = Dysk.objects.get(id=catalog.id_dysku.id)
    id_nadrzednego=catalog.id_katalogu_nadrzednego
    catalog.delete()

    catalog = Katalog.objects.get(id=id_nadrzednego.id)
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=id_nadrzednego.id)
    files = Document.objects.filter(id_katalogu=id_nadrzednego.id)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)

def upload(request, disk_id):
    dysk = Dysk.objects.get(id=disk_id)
    if request.user.is_authenticated:
        # Is it better to use @login_required ?
        username = request.user.username
    else:
        #catalog= Katalog.objects.get(id=catalog_id)
        username = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            s = dysk.rozmiar_zajety
            s = s+doc.myfile.size
            Dysk.objects.filter(id=disk_id).update(rozmiar_zajety=s)

            return render(request, 'pages/upload.html', {
               "form": DocumentForm(),
               "uploaded_file_url": doc.myfile.url,
               "username": username,
            })
    else:
        form = DocumentForm()
    return render(request, 'pages/upload.html', {"form": form})

def deleteFile(request, plik_id):
    file = Document.objects.get(id=plik_id)
    catalog = file.id_katalogu
    disk = catalog.id_dysku

    s = disk.rozmiar_zajety
    s = s - file.myfile.size
    Dysk.objects.filter(id=disk.id).update(rozmiar_zajety=s)

    file.myfile.delete()
    file.delete()
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)
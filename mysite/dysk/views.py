from django.shortcuts import render
from .models import Dysk, Katalog, Plik, Document, Widok, SchowekPlik
from django.contrib.auth.models import User
from .forms import DocumentForm
from django.shortcuts import get_object_or_404

# admin ZAQ!2wsx

def about(request):
    view1 = Widok.objects.get(nazwa="about.html_head")
    view2 = Widok.objects.get(nazwa="about.html")
    context = {'view1': view1,'view2': view2}
    return render(request, 'pages/about.html', context)

def profile(request):
    all_objects=Dysk.objects.all()
    view1 = Widok.objects.get(nazwa="profile.html_adding")
    view2 = Widok.objects.get(nazwa="profile.html_welcome")
    context={'all_objects': all_objects, 'view1': view1, 'view2': view2}
    return render(request,'pages/profile.html', context)

def disk(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id_dysku=disk, nazwa="root")
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog)
    files = Document.objects.filter(id_katalogu=catalog)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)

def diskDelete(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    disk.delete()
    # profile(request)
    all_objects=Dysk.objects.all()
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context={'all_objects': all_objects, 'view1': view1, 'view2': view2}
    return render(request,'pages/profile.html', context)

def catalog(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id=catalog_id)
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog_id)
    files = Document.objects.filter(id_katalogu=catalog)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)

def catalogNadrzedny(request, disk_id, catalog_id, catalog_nadrzedny_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id=catalog_id)
    catalogNadrzedny = Katalog.objects.get(id=catalog_nadrzedny_id)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': catalogNadrzedny}
    return render(request, 'pages/catalog.html', context=mydict)

def addStandard(request, user_id):
    u = User.objects.get(id=user_id)
    disk = Dysk()
    disk.rozmiar_calkowity=1
    disk.rozmiar_zajety=0
    disk.id_user=u
    disk.save()
    # profile(request)
    all_objects = Dysk.objects.all()
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context = {'all_objects': all_objects, 'view1': view1, 'view2': view2}
    root = Katalog()
    root.nazwa="root"
    root.id_dysku=disk
    root.sciezka_do_katalogu="/"
    root.save()
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
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context = {'all_objects': all_objects, 'view1': view1, 'view2': view2}
    root = Katalog()
    root.nazwa = "root"
    root.id_dysku = disk
    root.sciezka_do_katalogu = "/"
    root.save()
    return render(request, 'pages/profile.html', context)

def addCatalog(request, disk_id):
    disk = Dysk.objects.get(id=disk_id)
    all_objects = Katalog.objects.all()
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context = {'all_objects': all_objects, 'view1': view1, 'view2': view2}
    catalog = Katalog()
    catalog.nazwa = "new_catalog"
    catalog.id_dysku = disk
    catalog.sciezka_do_katalogu="/new_catalog"
    catalog.save()
    return render(request, 'pages/profile.html',context)

def changeNameFolder(request, folder_id):
    test = Katalog.objects.get(id=folder_id)
    test.nazwa = request.GET.get('changeFolder')
    test.save(update_fields=['nazwa'])
    all_objects = Katalog.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'pages/catalog.html', context)

def stopSharing(request, file_id):
    file= Document.objects.get(id=file_id)
    catalog= file.id_katalogu
    cat= catalog.id_katalogu_nadrzednego
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=cat.id)
    dysk= catalog.id_dysku
    disk = Dysk.objects.filter(id=dysk.id_dysku)
    file.udostepniony = False
    file.save(update_fields=['udostepniony'])
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context={'disk':disk, 'catalog': cat, 'files': file, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context)

def startSharing(request, file_id):
    file= Document.objects.get(id=file_id)
    catalog= file.id_katalogu
    cat= catalog.id_katalogu_nadrzednego
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=cat.id)
    dysk= catalog.id_dysku
    disk = Dysk.objects.filter(id=dysk.id_dysku)
    file.udostepniony = True
    file.save(update_fields=['udostepniony'])
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    context={'disk':disk, 'catalog': cat, 'files': file, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context)


def shareFile(request, file_id):
    file = Document.objects.get(id=file_id)
    context = {'file': file}
    return render(request, 'pages/shareFile.html', context)

def addCatalogNadrzedny(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id=disk_id)
    id_katalogu=Katalog.objects.get(id=catalog_id)
    catalog = Katalog()
    catalog.nazwa = request.GET.get('folder')
    catalog.id_dysku = disk
    catalog.sciezka_do_katalogu = "/new_catalog"
    catalog.id_katalogu_nadrzednego = id_katalogu

    id_nadrzednego=catalog.id_katalogu_nadrzednego
    catalog.save()

    cat = Katalog.objects.get(id=id_nadrzednego.id)
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=id_nadrzednego.id)
    files = Document.objects.filter(id_katalogu=id_nadrzednego.id)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': cat, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)

def deleteCatalog(request, catalog_id):

    catalog = Katalog.objects.get(id=catalog_id)
    disk = Dysk.objects.get(id=catalog.id_dysku.id)
    id_nadrzednego=catalog.id_katalogu_nadrzednego
    catalog.delete()

    catalog = Katalog.objects.get(id=id_nadrzednego.id)
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=id_nadrzednego.id)
    files = Document.objects.filter(id_katalogu=id_nadrzednego.id)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1, 'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)

def upload(request, disk_id, catalog_id):
    disk = Dysk.objects.get(id=disk_id)
    catalog = Katalog.objects.get(id=catalog_id)
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
            s = disk.rozmiar_zajety
            s = s+doc.myfile.size
            Dysk.objects.filter(id=disk_id).update(rozmiar_zajety=s)

            return render(request, 'pages/upload.html', {
               "form": DocumentForm(),
               "uploaded_file_url": doc.myfile.url,
               "username": username,
               "disk": disk,
               "catalog": catalog
            })
    else:
        form = DocumentForm()
    return render(request, 'pages/upload.html', {"form": form, "disk": disk, "catalog": catalog})

def deleteFile(request, plik_id):
    file = Document.objects.get(id=plik_id)
    catalog = file.id_katalogu
    disk = catalog.id_dysku

    s = disk.rozmiar_zajety
    s = s - file.myfile.size
    Dysk.objects.filter(id=disk.id).update(rozmiar_zajety=s)

    # przed usunieciem pliku sprawdzam, czy nie jest przypadkiem zapisany w schowku
    # jeżeli jest, to usuwam go ze schowka -> tak jest prościej
    if SchowekPlik.objects.filter(id=plik_id):
        p = SchowekPlik.objects.filter()[:1].get()
        p.delete()

    # przed usunieciem z /media przegladam tez, czy gdzieś nie ma kopii tego pliku, żeby nie spowodować błędu
    if Document.objects.filter(myfile = file.myfile).exists():
        file.delete()
    else:
        file.myfile.delete()
        file.delete()

    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog)
    files = Document.objects.filter(id_katalogu=catalog)
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs}
    return render(request, 'pages/catalog.html', context=mydict)

def copyFile(request, catalog_id, plik_id):
    catalog = Katalog.objects.get(id=catalog_id)
    disk = Dysk.objects.get(id=catalog.id_dysku.id)
    user = User.objects.get(id=disk.id_user.id)
    # opróżnianie schowka danego użytkownika
    if SchowekPlik.objects.filter(id_user=user).exists():
        p = SchowekPlik.objects.filter(id_user=user)[:1].get()
        p.delete()
    # p = SchowekFolder.objects.filter()[:1].get()
    # p.delete()

    # zapisanie kopii do schowka
    plik = Document.objects.get(id=plik_id)
    schowek = SchowekPlik()
    schowek.id_pliku = plik
    schowek.id_user = user
    schowek.save()

    # zwykłe wyswietlanie aktualnego katalogu
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog_id)
    files = Document.objects.filter(id_katalogu=catalog)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1,
              'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)

def pasteFile(request, disk_id, catalog_id):
    catalog = Katalog.objects.get(id=catalog_id)
    disk = Dysk.objects.get(id=disk_id)
    user = User.objects.get(id=disk.id_user.id)

    # sprawdzenie, czy dany użytkownik na pewno ma coś w schowku
    if SchowekPlik.objects.filter(id_user=user)[:1].exists():
        # przechywcenie ze schowka i odnalezienie pliku w obiektach Document
        plik_kopiowany = SchowekPlik.objects.filter(id_user=user)[:1].get()
        plik = Document.objects.get(id=plik_kopiowany.id_pliku.id)

        # tworzenie nowej kopii pliku
        plik_skopiowany = Document()
        # wklejamy go do aktualnego katalogu
        plik_skopiowany.id_katalogu = catalog
        plik_skopiowany.name = plik.name
        plik_skopiowany.typ_pliku = plik.typ_pliku
        plik_skopiowany.sciezka_do_pliku = plik.sciezka_do_pliku
        plik_skopiowany.myfile = plik.myfile
        plik_skopiowany.save()

        # opróżnienie schowka <- na razie zakomentowane, bo chyba po wklejeniu nie powinno usuwać się ze schowka
        # p.delete()

        # aktualizacja rozmiaru dysku
        s = disk.rozmiar_zajety
        s = s + plik.myfile.size
        Dysk.objects.filter(id=disk_id).update(rozmiar_zajety=s)

    # zwykłe wyświetlanie aktualnego katalogu
    sub_catalogs = Katalog.objects.filter(id_katalogu_nadrzednego=catalog_id)
    files = Document.objects.filter(id_katalogu=catalog)
    view1 = Widok.objects.get(nazwa="catalog.html_adding_folder")
    view2 = Widok.objects.get(nazwa="catalog.html_uploading_file")
    mydict = {'disk': disk, 'catalog': catalog, 'files': files, 'sub_catalogs': sub_catalogs, 'view1': view1,
              'view2': view2}
    return render(request, 'pages/catalog.html', context=mydict)


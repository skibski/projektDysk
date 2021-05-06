from django.contrib import admin

# from .models import Uzytkownik
from .models import Dysk
from .models import Katalog
from .models import Plik

# admin.site.register(Uzytkownik)
admin.site.register(Dysk)
admin.site.register(Katalog)
admin.site.register(Plik)

from django.contrib import admin

# from .models import Uzytkownik
from .models import Dysk
from .models import Katalog
from .models import Plik
from .models import Document

# admin.site.register(Uzytkownik)
admin.site.register(Dysk)
admin.site.register(Katalog)
admin.site.register(Plik)
admin.site.register(Document)

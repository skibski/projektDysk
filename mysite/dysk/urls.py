from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('addCatalog/<int:disk_id>/',views.addCatalog, name='addCatalog'),
    path('addCatalog/',views.addCatalog, name='addCatalog'),
    path('deleteCatalog/<int:catalog_id>/',views.deleteCatalog, name='deleteCatalog'),
    path('deleteCatalog/',views.deleteCatalog, name='deleteCatalog'),
    path('addStandard/<int:user_id>/',views.addStandard, name='addStandard'),
    path('addStandard',views.addStandard, name='addStandard'),
    path('addPremium/<int:user_id>/',views.addPremium, name='addPremium'),
    path('addPremium',views.addPremium, name='addPremium'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('disk/<int:disk_id>/',views.disk, name='disk'),
    path('disk/',views.disk, name='disk'),
    path('diskDelete/<int:disk_id>/',views.diskDelete, name='diskDelete'),
    path('diskDelete/',views.diskDelete, name='diskDelete'),
    path('catalog/<int:disk_id>/<int:catalog_id>/',views.catalog, name='catalog'),
    path('catalog/',views.catalog, name='catalog'),
]
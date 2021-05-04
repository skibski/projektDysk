from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('disk/<int:disk_id>/',views.disk, name='disk'),
    path('disk/',views.disk, name='disk'),
    path('catalog/<int:disk_id>/<int:catalog_id>/',views.catalog, name='catalog'),
    path('catalog/',views.catalog, name='catalog'),
]
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
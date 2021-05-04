from django.shortcuts import render
from .models import Dysk
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

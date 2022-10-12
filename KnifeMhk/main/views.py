from django.shortcuts import render
from .models import *

# Create your views here.


def base(request):
    types_ = Type.objects.all()
    posts = Knife.objects.all()
    return render(request, 'main/base.html' , context={'posts':posts , 'types' : types_ })


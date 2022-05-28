from django.shortcuts import render
from .models import *
# Create your views here.
def base(request):

    posts = Knife.objects.all()
    return render(request, 'main/base.html' , context={'posts':posts})

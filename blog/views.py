from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Plato

def plato_list(request):
    plato =Plato.objects.all()
    return render(request,'blog/plato_list.html',{'plato':plato})
# Create your views here.

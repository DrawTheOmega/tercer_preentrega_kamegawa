from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.



def inicioApp(request):
    return render(request, "Appcoder/inicio.html")

def vendedores(request):
    return render(request, "Appcoder/vendedores.html")

def productos(request):
    return render(request, "Appcoder/productos.html")
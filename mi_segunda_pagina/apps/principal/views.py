from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import *
# Create your views here.

def  index(request):
    return render(request, "principal/index.html")

def maquinas(request):
    return render(request, "principal/maquinas.html")

def planes(request):
    return render(request, "principal/planes.html")

def sedes(request):
    return render(request, "principal/sedes.html")

def filosofia(request):
    return render(request, "principal/filosofia.html")

def quienes_somos(request):
    return render(request, "principal/quienes_somos.html")

def registrado(request):
    return render(request, "principal/registrado.html")



class CustomLoginView(LoginView):
    authentication_form= CustomAuthenticationForm
    template_name= "principal/login.html"

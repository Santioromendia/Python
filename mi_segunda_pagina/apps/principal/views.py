from django.shortcuts import render

# Create your views here.

def  index(request):
    return render(request, "principal/index.html")

def planes(request):
    return render(request, "principal/planes.html")

def sedes(request):
    return render(request, "principal/sedes.html")

def filosofia(request):
    return render(request, "principal/filosofia.html")

def quienes_somos(request):
    return render(request, "principal/quienes_somos.html")


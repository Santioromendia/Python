from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from . import models, forms


# Create your views here.

def  index(request):
    return render(request, "cliente/index.html")

def cliente_list (request):
    clientes=models.cliente.objects.all()
    return render(request, "cliente/cliente_list.html", {"clientes": clientes})

def cliente_create(request) -> HttpResponse:
    if request.method=="POST":
        form=forms.clienteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else:
        form=forms.clienteform()
    return render(request, "cliente/cliente_create.html",{"form":form})


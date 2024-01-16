from django.shortcuts import redirect, render, HttpResponse
from . import models
from . import forms


def index(request):
    return render(request, "cliente/index.html")

def pais_list(request):
    paises = models.pais.objects.all()
    context = {"paises": paises}
    return render(request, "cliente/pais_list.html", context)

def comida_list(request):
    comidas = models.comida.objects.all()
    context = {"comidas": comidas}
    return render(request, "cliente/comida_list", context)


def cliente_list(request):
    cliente = models.cliente.objects.all()
    context = {"clientes": cliente}
    return render(request, "cliente/cliente_list.html", context)

def cliente_create(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else:
        form = forms.clienteForm()
        return render(request, "cliente/cliente_create.html", {"form" : form})
    
    

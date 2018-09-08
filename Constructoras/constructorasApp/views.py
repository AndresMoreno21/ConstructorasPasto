from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.
def inicio(request):
    return render(request, 'base.html')

def constructoras_base(request):
    constructoras = Constructora.objects.all()
    context = {'constructoras_list': constructoras}
    return render(request, 'base.html', context)

def edificos_detail(request, id):
    edificios = Constructora.objects.get(id= id)
    context = {'object': edificios}
    return render(request, 'edificios.html', context)

def apartamentos_detail(request, pk):
    apartamentos = Edificio.objects.get(id= pk)
    context = {'apartamentos': apartamentos}
    return render(request, 'apartamentos.html', context)

def carrete_detail(request, pk):
    fotos = Apartamento.objects.get(id= pk)
    context = {'fotos': fotos}
    return render(request, 'carreteFotos.html', context)


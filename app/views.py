from django.shortcuts import render
from app.models import Catalogo
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'home.html')

class CatalogoCreate(CreateView):
    model = Catalogo
    fields = ['servico','valor']
    template_name = 'admin/form.html'
    success_url = reverse_lazy('catalogo')

class CatalogoList(ListView):
    model = Catalogo
    template_name = 'catalogo.html'

def agendamento(request):
    return render(request,'agendamento.html')
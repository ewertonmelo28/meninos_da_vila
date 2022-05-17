from django.shortcuts import render
from app.models import Catalogo
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'home.html')

def catalogo(request):
    data = {"db": Catalogo.objects.all()}
    return render(request,'catalogo.html', data)

class CatalogoCreate(CreateView):
    model = Catalogo
    fields = ['servico','valor']
    template_name = 'admin/form.html'
    success_url = reverse_lazy('catalogo')


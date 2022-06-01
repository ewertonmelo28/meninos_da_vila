from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView
from app.models import Catalogo
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

from django.contrib.auth import get_user_model

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'home.html'

index = IndexView.as_view()

def home(request):
    return render(request,'home.html')
    
def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

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


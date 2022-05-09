from django.shortcuts import render
from app.models import Catalogo
# Create your views here.

def home(request):
    return render(request,'home.html')

def catalogo(request):
    data = {}
    data['db'] = Catalogo.objects.all()
    data['i'] = 1
    return render(request,'catalogo.html', data)
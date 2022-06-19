"""meninos_da_vila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path as url
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView
from app.views import CatalogoDelete, CatalogoList, CatalogoCreate, CatalogoUpdate, ProfissionalDelete , ProfissionalList, ProfissionalCreate, ProfissionalUpdate

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name="index"),     
    url(r'^contato/$', views.contact, name="contact"),
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'), 
    url(r'^sair/$', LogoutView.as_view(next_page = 'index'), name='logout'),    
    url(r'^conta/', include('accounts.urls', namespace='accounts')),  
    path('catalogo',CatalogoList.as_view(),name='catalogo'),
    path('catalogo/criar/',CatalogoCreate.as_view(),name='catalogo-criar'),
    path('catalogo/editar/<int:pk>/',CatalogoUpdate.as_view(),name='catalogo-editar'),
    path('catalogo/excluir/<int:pk>/',CatalogoDelete.as_view(),name='catalogo-excluir'),
    path('agendamento',ProfissionalList.as_view(),name='agendamento'),
    path('agendamento/criar/',ProfissionalCreate.as_view(),name='agendamento-criar'),
    path('agendamento/editar/<int:pk>/',ProfissionalUpdate.as_view(),name='agendamento-editar'),
    path('agendamento/excluir/<int:pk>/',ProfissionalDelete.as_view(),name='agendamento-excluir'),
    url(r'^admin/', admin.site.urls),
    
]

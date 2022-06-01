from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome') 
    lastname = forms.CharField(label='Sobrenome')   
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']      
        lastname = self.cleaned_data['lastname']     
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, lastname, email, message)
        send_mail(
            'Contato Projeto Meninos-da-Vila', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]       
        )

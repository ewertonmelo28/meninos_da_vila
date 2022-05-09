from django.db import models

# Create your models here.

class Catalogo(models.Model):
    servico = models.CharField(max_length=150)
    valor = models.FloatField()
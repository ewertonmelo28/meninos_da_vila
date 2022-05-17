from django.db import models

# Create your models here.

class Catalogo(models.Model):
    servico = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return "{} {}".format(self.servico, self.valor)
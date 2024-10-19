from django.db import models
from sale.models import Sale

class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    birthdate = models.DateField(verbose_name='Data de Nascimento')
    created_at = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')
    email = models.EmailField(null=True, verbose_name='Email')
    last_purchase = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True, related_name='last_purchase')

    def __str__(self):
        return self.name

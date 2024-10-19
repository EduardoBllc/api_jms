from django.db import models

class Product(models.Model):
    class Metal(models.TextChoices):
        GOLD = 'Gold'
        SILVER = 'Silver'

    class Modality(models.TextChoices):
        CHILD = 'Child'
        ADULT = 'Adult'

    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    metal = models.TextField(choices=Metal, verbose_name='Metal')
    codigo_fabrica = models.CharField(max_length=100, verbose_name='Código da Fábrica')
    data_compra = models.DateField(verbose_name='Data de compra')
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de custo')
    preco_prazo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço a vista')
    preco_vista = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço a prazo')


class Supplier(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')


from django.db import models

class Product(models.Model):
    class Metal(models.TextChoices):
        GOLD = 'Gold'
        SILVER = 'Silver'

    class Modality(models.TextChoices):
        CHILD = 'Child'
        ADULT = 'Adult'

    description = models.CharField(max_length=100, verbose_name='Description')
    metal = models.TextField(choices=Metal, verbose_name='Metal')
    supplier_code = models.CharField(max_length=100, verbose_name='Supplier code')
    purchase_date = models.DateField(verbose_name='Purchase date')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cost price')
    cash_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cash price')
    deffered_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Defered price')


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')


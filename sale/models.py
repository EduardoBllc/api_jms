from django.db import models
from django.db.models import ForeignKey
from django.db.models.signals import post_delete
from django.dispatch import receiver

from customer.models import Customer
from product.models import Product


class Sale(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'Cash'
        PIX = 'Pix'
        CREDIT_CARD = 'Credit Card'
        DEFERRED = 'Deferred'

    sale_date = models.DateField(auto_now_add=True, verbose_name="Sale date")
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, verbose_name="Customer")
    payment_method = models.IntegerField(choices=PaymentMethod, verbose_name="Payment method")

@receiver(post_delete, sender=Sale)
def atualizar_ultima_compra(sender, instance, **kwargs):
    cliente = instance.cliente
    # Busca a venda mais recente após a exclusão da venda atual
    ultima_venda = cliente.vendas.exclude(id=instance.id).order_by('-sale_date').first()

    # Atualiza o campo 'ultima_compra' do cliente
    cliente.ultima_compra = ultima_venda
    cliente.save()

class SaleProduct(models.Model):
    sale = ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)



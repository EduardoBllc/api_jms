from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from customer.models import Customer


class Sale(models.Model):
    purchase_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

@receiver(post_delete, sender=Sale)
def atualizar_ultima_compra(sender, instance, **kwargs):
    cliente = instance.cliente
    # Busca a venda mais recente após a exclusão da venda atual
    ultima_venda = cliente.vendas.exclude(id=instance.id).order_by('-purchase_date').first()

    # Atualiza o campo 'ultima_compra' do cliente
    cliente.ultima_compra = ultima_venda
    cliente.save()

from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    birthdate = models.DateField(verbose_name=_('Birthdate'))
    created_at = models.DateField(auto_now_add=True, verbose_name='Created date')
    email = models.EmailField(null=True, verbose_name='Email')
    last_purchase = models.ForeignKey('sale.Sale',
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name='last_purchase',
                                      verbose_name=_('Last purchase'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

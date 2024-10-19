from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    birthdate = models.DateField(verbose_name='Birthdate')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created date')
    email = models.EmailField(null=True, verbose_name='Email')
    last_purchase = models.ForeignKey('sale.Sale',
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name='last_purchase',
                                      verbose_name='Last purchase')

    def __str__(self):
        return self.name

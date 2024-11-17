from django.db import models
from django.utils.translation import gettext_lazy as _


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'supplier'
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

class Product(models.Model):
    class Metal(models.TextChoices):
        GOLD = 'Gold', _("Gold")
        SILVER = 'Silver', _("Silver")

    class Modality(models.TextChoices):
        CHILD = 'Child', _("Child")
        ADULT = 'Adult', _("Adult")

    class Category(models.TextChoices):
        EARRING = 'Earring', _("Earring")
        NECKLACE = 'Necklace', _("Necklace")
        RING = 'Ring', _("Ring")
        BRACELET = 'Bracelet', _("Bracelet")
        PENDANT = 'Pendant', _("Pendant")
        CHOKER = 'Choker', _("Choker")

    description = models.CharField(max_length=100, verbose_name=_("Description"))
    metal = models.TextField(choices=Metal, verbose_name=_("Metal"), null=True)
    category = models.TextField(choices=Category, verbose_name=_("Category"), null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name=_("Supplier"))
    supplier_code = models.CharField(max_length=100, verbose_name=_("Supplier code"))
    purchase_date = models.DateField(verbose_name=_("Purchase date"))
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Cost price"))
    cash_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Cash price"))
    deffered_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Deferred price"))

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'product'
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
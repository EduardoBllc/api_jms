from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SaleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sale'
    verbose_name = _('Sale')
    verbose_name_plural = _('Sales')

from django.contrib import admin

from sale.models import Sale, SaleProduct

# Register your models here.
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass

@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    pass
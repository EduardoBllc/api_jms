from django.contrib import admin

from product.models import Product, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
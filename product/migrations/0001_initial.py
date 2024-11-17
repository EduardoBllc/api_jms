# Generated by Django 5.1.2 on 2024-10-19 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('metal', models.TextField(choices=[('Gold', 'Gold'), ('Silver', 'Silver')], null=True, verbose_name='Metal')),
                ('category', models.TextField(choices=[('Earring', 'Earring'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Bracelet', 'Bracelet')], null=True, verbose_name='Category')),
                ('supplier_code', models.CharField(max_length=100, verbose_name='Supplier code')),
                ('purchase_date', models.DateField(verbose_name='Purchase date')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost price')),
                ('cash_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cash price')),
                ('deffered_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Defered price')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.supplier', verbose_name='Supplier')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
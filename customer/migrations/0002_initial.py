# Generated by Django 5.1.2 on 2024-10-19 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_purchase', to='sale.sale', verbose_name='Last purchase'),
        ),
    ]
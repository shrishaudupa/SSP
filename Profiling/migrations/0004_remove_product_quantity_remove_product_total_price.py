# Generated by Django 4.2.5 on 2024-03-20 17:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Profiling", "0003_product_quantity_product_total_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="product",
            name="total_price",
        ),
    ]
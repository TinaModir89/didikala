# Generated by Django 5.1 on 2024-10-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0024_alter_clothes_product_sale_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes_product',
            old_name='ia_sale',
            new_name='is_sale',
        ),
        migrations.RenameField(
            model_name='digital_product',
            old_name='ia_sale',
            new_name='is_sale',
        ),
    ]

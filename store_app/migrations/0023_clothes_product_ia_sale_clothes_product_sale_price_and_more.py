# Generated by Django 5.1 on 2024-10-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0022_remove_description_description_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes_product',
            name='ia_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='sale_price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='ia_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='sale_price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]

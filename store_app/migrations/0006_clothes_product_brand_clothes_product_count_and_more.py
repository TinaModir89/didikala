# Generated by Django 5.1 on 2024-09-16 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_digital_product_category_clothes_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes_product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store_app.brand'),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store_app.brand'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

# Generated by Django 5.1 on 2024-09-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_clothes_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes_product',
            name='image',
            field=models.ImageField(null=True, upload_to='clothes_image'),
        ),
    ]

# Generated by Django 5.1 on 2024-09-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0018_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes_product',
            name='is_suggested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='is_suggested',
            field=models.BooleanField(default=False),
        ),
    ]

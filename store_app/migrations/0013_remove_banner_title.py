# Generated by Django 5.1 on 2024-09-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='title',
        ),
    ]

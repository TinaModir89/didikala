# Generated by Django 5.1 on 2024-09-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0016_rename_field_brand_name_rename_field_color_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='store/images'),
        ),
    ]

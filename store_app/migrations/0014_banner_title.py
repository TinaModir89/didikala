# Generated by Django 5.1 on 2024-09-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0013_remove_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

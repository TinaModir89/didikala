# Generated by Django 5.1 on 2024-09-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_banner_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='clothes_product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='digital_product',
            name='category',
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='category',
            field=models.ManyToManyField(to='store_app.category'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='category',
            field=models.ManyToManyField(to='store_app.category'),
        ),
    ]

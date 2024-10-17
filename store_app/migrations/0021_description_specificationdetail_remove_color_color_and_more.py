# Generated by Django 5.1 on 2024-10-06 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('store_app', '0020_alter_image_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='color',
        ),
        migrations.RemoveField(
            model_name='color',
            name='product',
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='code_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='reviews',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='code_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='colors',
            field=models.ManyToManyField(blank=True, related_name='digital_colors', to='store_app.color'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='reviews',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='descriptions',
            field=models.ManyToManyField(blank=True, related_name='clothes_descriptions', to='store_app.description'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='descriptions',
            field=models.ManyToManyField(blank=True, related_name='digital_descriptions', to='store_app.description'),
        ),
        migrations.CreateModel(
            name='DetailDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_descriptions', to='store_app.image')),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='description_detail',
            field=models.ManyToManyField(related_name='descriptions', to='store_app.detaildescription'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_app_favorites', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store_app.category')),
            ],
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='special_features',
            field=models.ManyToManyField(related_name='clothes_features', to='store_app.specialfeature'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='special_features',
            field=models.ManyToManyField(related_name='digital_features', to='store_app.specialfeature'),
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('specification_detail', models.ManyToManyField(related_name='specifications', to='store_app.specificationdetail')),
            ],
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='specifications',
            field=models.ManyToManyField(related_name='clothes_specifications', to='store_app.specifications'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='specifications',
            field=models.ManyToManyField(related_name='digital_specifications', to='store_app.specifications'),
        ),
    ]

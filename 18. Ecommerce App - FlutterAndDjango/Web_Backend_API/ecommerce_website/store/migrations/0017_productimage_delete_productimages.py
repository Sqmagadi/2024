# Generated by Django 5.0.2 on 2024-05-12 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]

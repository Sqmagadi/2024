# Generated by Django 5.0.2 on 2024-03-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_product',
            field=models.BooleanField(default=True),
        ),
    ]

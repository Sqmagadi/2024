# Generated by Django 5.0.6 on 2024-05-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

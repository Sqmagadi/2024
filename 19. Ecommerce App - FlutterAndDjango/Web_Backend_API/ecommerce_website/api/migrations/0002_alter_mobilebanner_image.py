# Generated by Django 5.0.2 on 2024-05-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilebanner',
            name='image',
            field=models.ImageField(upload_to='uploads/banners/', verbose_name='Image'),
        ),
    ]
# Generated by Django 3.2.7 on 2021-12-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_termine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=32, verbose_name='Produkt Name'),
        ),
    ]

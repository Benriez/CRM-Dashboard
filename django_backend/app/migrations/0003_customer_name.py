# Generated by Django 3.2.7 on 2021-11-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Firmenname'),
        ),
    ]

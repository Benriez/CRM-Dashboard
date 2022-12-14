# Generated by Django 3.2.7 on 2021-12-12 18:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211211_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Termine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termintyp', models.CharField(blank=True, max_length=128, null=True, verbose_name='Termintyp')),
                ('menge', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True, max_length=1000, verbose_name='Kommentar')),
                ('erstellt', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('datum', models.DateTimeField(blank=True, null=True)),
                ('kunde', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('produkt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
            options={
                'verbose_name': 'Termin',
                'verbose_name_plural': 'Termine',
            },
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Firmenname')),
                ('website', models.CharField(blank=True, max_length=50, null=True, verbose_name='Firmenwebseite')),
                ('anrede', models.CharField(blank=True, max_length=20, null=True, verbose_name='Anrede')),
                ('vorname_ansprechpartner', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vorname Ansprechpartner')),
                ('nachname_ansprechpartner', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nachname Ansprechpartner')),
                ('email_ansprechpartner', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email Ansprechpartner')),
                ('phone_ansprechpartner', models.CharField(blank=True, max_length=20, verbose_name='Telefon Ansprechpartner')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telefon')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Straße')),
                ('haus_nr', models.CharField(blank=True, max_length=10, verbose_name='Haus-nr.')),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='PLZ')),
                ('ort', models.CharField(blank=True, max_length=10, verbose_name='Ort')),
                ('billing_address', models.CharField(blank=True, max_length=300, verbose_name='Rechnungsadresse')),
                ('comment', models.TextField(blank=True, max_length=1000, verbose_name='Kommentar')),
            ],
            options={
                'verbose_name': 'Kunden',
                'verbose_name_plural': 'Kunden',
            },
        ),
    ]

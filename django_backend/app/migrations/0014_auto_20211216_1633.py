# Generated by Django 3.2.7 on 2021-12-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_signale'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'CRM-Integration',
                'verbose_name_plural': 'CRM-Integration',
            },
        ),
        migrations.CreateModel(
            name='Kommunikationstool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Kommunikationstool',
                'verbose_name_plural': 'Kommunikationstool',
            },
        ),
        migrations.CreateModel(
            name='Warenwirtschaftssystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Warenwirtschaftssystem',
                'verbose_name_plural': 'Warenwirtschaftssystem',
            },
        ),
        migrations.AlterModelOptions(
            name='signale',
            options={'verbose_name': 'Kundensignal', 'verbose_name_plural': 'Kundensignale'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='haus_nr',
            field=models.CharField(blank=True, max_length=10, verbose_name='Haus-Nr.'),
        ),
        migrations.AlterField(
            model_name='signale',
            name='auftragstyp',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Signaltyp'),
        ),
    ]

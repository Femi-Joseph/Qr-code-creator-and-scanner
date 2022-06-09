# Generated by Django 3.2.7 on 2021-12-29 09:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientdataqrexe2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.TextField(default=None, null=True)),
                ('hadcovid19', models.CharField(max_length=5)),
                ('coviddate', models.DateField(blank=True, default=None, null=True)),
                ('vaccinated', models.CharField(max_length=5)),
                ('first_dose', models.DateField(blank=True, null=True)),
                ('second_dose', models.DateField(blank=True, null=True)),
                ('contact_covid', models.CharField(max_length=5)),
                ('cotact_date', models.DateField(blank=True, null=True)),
                ('passanger', models.CharField(max_length=5)),
                ('covid_test', models.CharField(max_length=5)),
                ('photo', models.ImageField(upload_to='client_data')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('qrcode', models.ImageField(upload_to='client_data\\qrcode')),
                ('todaydate', models.DateField(default=datetime.date(2021, 12, 29))),
                ('status', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-12 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0024_alter_clientdataqrexe2_todaydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdataqrexe2',
            name='todaydate',
            field=models.DateField(default=datetime.date(2022, 5, 12)),
        ),
    ]

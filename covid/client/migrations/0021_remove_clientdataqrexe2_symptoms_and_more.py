# Generated by Django 4.0 on 2022-03-03 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_alter_clientdataqrexe2_todaydate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdataqrexe2',
            name='symptoms',
        ),
        migrations.RemoveField(
            model_name='clientdocument',
            name='qrvideo',
        ),
    ]

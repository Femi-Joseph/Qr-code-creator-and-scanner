# Generated by Django 4.0 on 2022-01-22 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_alter_clientdataqrexe2_todaydate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdataqrexe2',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientdocument',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='clientdataqrexe2',
        ),
        migrations.DeleteModel(
            name='clientdocument',
        ),
    ]

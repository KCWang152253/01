# Generated by Django 2.1.7 on 2020-07-13 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wheel',
            name='isDelete',
        ),
    ]

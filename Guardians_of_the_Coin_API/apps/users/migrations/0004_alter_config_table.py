# Generated by Django 4.0.3 on 2022-04-14 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_config'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='config',
            table='user_config',
        ),
    ]
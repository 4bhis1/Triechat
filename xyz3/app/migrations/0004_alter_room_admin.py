# Generated by Django 3.2.1 on 2021-11-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_room_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='admin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
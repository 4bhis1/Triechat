# Generated by Django 3.2.1 on 2021-11-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_message_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='admin',
            field=models.CharField(default=1234, max_length=100),
            preserve_default=False,
        ),
    ]

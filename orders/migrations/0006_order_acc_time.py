# Generated by Django 3.2.16 on 2022-12-09 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20221209_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='acc_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_myhman_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='myhman',
            name='now',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-17 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='station',
            name='last_cleaned_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 0, 9, 45, 404663)),
        ),
    ]

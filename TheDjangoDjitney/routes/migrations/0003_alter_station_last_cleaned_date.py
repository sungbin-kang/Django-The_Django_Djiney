# Generated by Django 3.2.9 on 2021-11-17 00:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20211117_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='last_cleaned_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

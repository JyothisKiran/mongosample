# Generated by Django 4.1.10 on 2023-07-19 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 5.0.6 on 2024-08-07 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passes',
            name='slot',
        ),
    ]
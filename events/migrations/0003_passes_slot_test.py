# Generated by Django 5.0.6 on 2024-08-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_passes_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='passes',
            name='slot_test',
            field=models.IntegerField(default=0),
        ),
    ]

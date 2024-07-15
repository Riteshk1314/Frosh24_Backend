# Generated by Django 5.0.6 on 2024-07-13 11:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_scanned'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
    ]

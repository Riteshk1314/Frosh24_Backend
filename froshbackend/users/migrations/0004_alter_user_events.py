# Generated by Django 5.0.6 on 2024-06-27 20:59

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=models.JSONField(blank=True, default=users.models.default_events),
        ),
    ]

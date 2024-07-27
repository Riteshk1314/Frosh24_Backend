# Generated by Django 5.0.6 on 2024-07-26 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0001_initial'),
        ('users', '0022_user_qr_code_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='hoods.hood'),
        ),
    ]

# Generated by Django 5.0.7 on 2024-09-01 19:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

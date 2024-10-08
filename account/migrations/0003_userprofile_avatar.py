# Generated by Django 5.0.7 on 2024-08-30 16:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='default_image_id_or_url', max_length=255, verbose_name='avatar'),
        ),
    ]

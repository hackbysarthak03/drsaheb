# Generated by Django 5.0.7 on 2024-09-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_alter_doctorprofile_degree_alter_doctorprofile_fees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='room_id',
            field=models.CharField(default='--', max_length=100),
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-19 05:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_userprofile_xp_userprofile_lvl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userID',
            field=models.CharField(default=uuid.UUID('5d03c027-5d57-4112-9b47-d564ef50c6da'), max_length=255, unique=True),
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-19 11:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_userprofile_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_profiles', to='server.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userID',
            field=models.CharField(default=uuid.UUID('09eec4f7-5c1b-44f5-aa68-11d5c97d6c56'), max_length=255, unique=True),
        ),
    ]

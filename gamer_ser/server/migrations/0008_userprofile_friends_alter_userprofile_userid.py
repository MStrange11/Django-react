# Generated by Django 5.0.7 on 2024-07-20 06:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_remove_userprofile_friends_alter_userprofile_userid'),
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
            field=models.CharField(default=uuid.UUID('3af8cb35-da69-466d-b3a6-c729ca498aa6'), max_length=255, unique=True),
        ),
    ]
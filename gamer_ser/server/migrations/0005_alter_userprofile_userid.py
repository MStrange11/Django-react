# Generated by Django 5.0.7 on 2024-07-19 05:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_userprofile_user_alter_userprofile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userID',
            field=models.CharField(default=uuid.UUID('4520df13-5821-4112-a8cf-8311e3e22a9d'), max_length=255, unique=True),
        ),
    ]
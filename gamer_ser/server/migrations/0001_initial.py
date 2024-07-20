# Generated by Django 5.0.7 on 2024-07-19 04:27

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(default=uuid.UUID('19c0535e-8aff-4628-952d-6ac340981d63'), max_length=255, unique=True)),
                ('current_state', models.CharField(default='ideal', max_length=255)),
                ('img', models.CharField(default='https://cdn-icons-png.flaticon.com/512/5281/5281619.png', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

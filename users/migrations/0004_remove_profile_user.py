# Generated by Django 4.2.2 on 2024-05-29 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]

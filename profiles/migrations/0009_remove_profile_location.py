# Generated by Django 3.2.23 on 2023-11-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]

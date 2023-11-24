# Generated by Django 3.2.23 on 2023-11-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pseudonym',
            field=models.CharField(default='pseudonym', help_text='Enter the name you would like to be known as to ALL users', max_length=100),
        ),
    ]

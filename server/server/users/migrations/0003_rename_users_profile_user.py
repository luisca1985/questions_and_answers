# Generated by Django 3.2.11 on 2022-01-07 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='users',
            new_name='user',
        ),
    ]

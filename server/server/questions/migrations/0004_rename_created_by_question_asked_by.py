# Generated by Django 3.2.11 on 2022-01-07 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='created_by',
            new_name='asked_by',
        ),
    ]

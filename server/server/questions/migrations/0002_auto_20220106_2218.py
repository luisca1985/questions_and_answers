# Generated by Django 3.2.11 on 2022-01-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('detail', models.CharField(default='detail', max_length=500, verbose_name='Answer detail')),
                ('is_correct', models.BooleanField(default=False, help_text='This is the correct answer select by the user who asked the question.', verbose_name='this is the correct answer')),
            ],
            options={
                'ordering': ['-is_correct', '-modified', '-created'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='answers_made',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='detail',
            field=models.CharField(default='detail', max_length=500, verbose_name='Question detail'),
        ),
        migrations.AddField(
            model_name='question',
            name='is_closed',
            field=models.BooleanField(default=False, help_text='The question has been closed by the user.', verbose_name='closed question'),
        ),
        migrations.AddField(
            model_name='question',
            name='is_public',
            field=models.BooleanField(default=True, help_text='The question has been hidden.', verbose_name='public question'),
        ),
        migrations.AddField(
            model_name='question',
            name='is_resolved',
            field=models.BooleanField(default=False, help_text='The question has been resolved by other user.', verbose_name='resolved question'),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='title', max_length=140, verbose_name='question title'),
        ),
    ]
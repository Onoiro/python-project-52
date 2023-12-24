# Generated by Django 4.2.7 on 2023-12-24 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ID',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9.@_+-]+$')]),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20180521_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='unique_id',
            new_name='qid',
        ),
    ]

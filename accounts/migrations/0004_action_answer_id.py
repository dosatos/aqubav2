# Generated by Django 2.0.5 on 2018-05-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180521_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='answer_id',
            field=models.IntegerField(default=0),
        ),
    ]

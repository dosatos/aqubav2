# Generated by Django 2.0.5 on 2018-08-31 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180831_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='correct',
            field=models.IntegerField(choices=[(1, 0), (1, 0)], default=0),
        ),
    ]
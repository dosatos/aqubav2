# Generated by Django 2.0.5 on 2018-08-31 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='correct',
            field=models.IntegerField(choices=[(True, 1), (False, 0)], default=0),
        ),
    ]
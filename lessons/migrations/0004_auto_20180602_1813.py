# Generated by Django 2.0.5 on 2018-06-02 18:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20180602_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
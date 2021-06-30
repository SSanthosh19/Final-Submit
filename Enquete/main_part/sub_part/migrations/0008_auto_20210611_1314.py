# Generated by Django 3.2.3 on 2021-06-11 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_alter_uquest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editsurvey',
            name='effect',
            field=models.CharField(choices=[('Effect-1', 'Effect-1'), ('Effect-2', 'Effect-2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='uquest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

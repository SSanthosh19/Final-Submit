# Generated by Django 3.2.3 on 2021-06-29 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0024_uquest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uquest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Date'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-29 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0026_alter_addsurvey_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Date'),
        ),
    ]
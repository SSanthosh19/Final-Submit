# Generated by Django 3.2.3 on 2021-06-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0016_auto_20210625_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addsurvey',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0014_auto_20210624_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edituser',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

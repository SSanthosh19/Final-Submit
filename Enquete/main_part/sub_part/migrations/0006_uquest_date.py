# Generated by Django 3.2.3 on 2021-06-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_alter_edit_testimonials_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uquest',
            name='date',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-29 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0019_alter_add_testimonials_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='uquest',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

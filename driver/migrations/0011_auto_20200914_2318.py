# Generated by Django 3.0.8 on 2020-09-14 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0010_auto_20200906_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='StartTime',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-14 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0011_auto_20200914_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='StartTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 23, 27, 22, 732860)),
        ),
    ]
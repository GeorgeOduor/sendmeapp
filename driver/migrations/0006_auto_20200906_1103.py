# Generated by Django 3.0.8 on 2020-09-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_auto_20200906_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='EndTime',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-06 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_auto_20200906_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='JourneyStat',
            new_name='From',
        ),
        migrations.RenameField(
            model_name='journey',
            old_name='JourneyStop',
            new_name='To',
        ),
    ]

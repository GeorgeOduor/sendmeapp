# Generated by Django 3.1.3 on 2021-04-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0032_journey_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='Duration',
            field=models.IntegerField(null=True),
        ),
    ]
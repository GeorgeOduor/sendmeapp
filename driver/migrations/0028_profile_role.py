# Generated by Django 3.1.3 on 2021-03-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0027_profile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Role',
            field=models.CharField(choices=[('Admin', 'Administartor'), ('Driver', 'Driver')], max_length=10, null=True),
        ),
    ]

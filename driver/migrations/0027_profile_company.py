# Generated by Django 3.1.3 on 2021-03-31 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0026_vehicle_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.companyprofile'),
        ),
    ]

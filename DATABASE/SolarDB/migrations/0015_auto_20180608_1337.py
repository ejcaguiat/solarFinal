# Generated by Django 2.0.5 on 2018-06-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0014_leaseproperty_numofyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaseproperty',
            name='advPaymentDate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear',
            field=models.FloatField(default=0),
        ),
    ]
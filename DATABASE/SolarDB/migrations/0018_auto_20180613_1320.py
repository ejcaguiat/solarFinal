# Generated by Django 2.0.5 on 2018-06-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0017_auto_20180613_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaseproperty',
            name='year10sum',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='year15sum',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='year20sum',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='year25sum',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='year30sum',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='year5sum',
            field=models.FloatField(default=0),
        ),
    ]
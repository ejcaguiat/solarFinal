# Generated by Django 2.0.3 on 2018-05-28 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('barangay', models.CharField(max_length=255)),
            ],
        ),
    ]

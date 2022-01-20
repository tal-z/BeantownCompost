# Generated by Django 4.0.1 on 2022-01-19 17:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DropoffLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=100)),
                ('location_name', models.CharField(max_length=100)),
                ('location_description', models.CharField(max_length=500)),
                ('location_address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
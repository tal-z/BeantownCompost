# Generated by Django 4.0.1 on 2022-01-19 22:34

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0005_alter_dropofflocation_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropofflocation',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=None, srid=4326),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-21 03:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0009_correctdropofflocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteDropoffLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=1000)),
                ('zip', models.CharField(max_length=1000)),
                ('x', models.FloatField(default=None)),
                ('y', models.FloatField(default=None)),
                ('point', django.contrib.gis.db.models.fields.PointField(default=None, null=True, srid=4326)),
            ],
        ),
    ]
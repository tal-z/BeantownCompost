# Generated by Django 4.0.1 on 2022-02-06 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0022_alter_dropofflocation_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropofflocation',
            name='point',
        ),
    ]
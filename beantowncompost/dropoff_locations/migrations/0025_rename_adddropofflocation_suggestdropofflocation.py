# Generated by Django 4.0.1 on 2022-02-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0024_dropofflocation_point'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddDropoffLocation',
            new_name='SuggestDropoffLocation',
        ),
    ]

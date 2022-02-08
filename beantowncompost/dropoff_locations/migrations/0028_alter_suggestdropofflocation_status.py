# Generated by Django 4.0.1 on 2022-02-08 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0027_suggestdropofflocation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestdropofflocation',
            name='status',
            field=models.CharField(choices=[('awaiting review', 'Awaiting Review'), ('addded to map', 'Added to Map'), ('denied', 'Denied')], default='Awaiting Review', max_length=25),
        ),
    ]

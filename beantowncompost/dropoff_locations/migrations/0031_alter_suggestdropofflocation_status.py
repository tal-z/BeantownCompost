# Generated by Django 4.0.1 on 2022-02-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locations', '0030_alter_suggestdropofflocation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestdropofflocation',
            name='status',
            field=models.CharField(default='Awaiting Review', max_length=100),
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0010_delete_managerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='managersitepermission',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

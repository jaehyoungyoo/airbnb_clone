# Generated by Django 2.1.8 on 2019-06-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20190601_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenity',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='location_info',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

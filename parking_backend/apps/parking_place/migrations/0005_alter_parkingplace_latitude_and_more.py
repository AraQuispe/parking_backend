# Generated by Django 4.1.2 on 2022-11-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_place', '0004_alter_parkingplace_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingplace',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='parkingplace',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]

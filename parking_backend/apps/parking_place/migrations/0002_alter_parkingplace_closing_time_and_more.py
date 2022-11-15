# Generated by Django 4.1.2 on 2022-11-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingplace',
            name='closing_time',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='parkingplace',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=9),
        ),
        migrations.AlterField(
            model_name='parkingplace',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=9),
        ),
        migrations.AlterField(
            model_name='parkingplace',
            name='opening_time',
            field=models.TextField(max_length=15),
        ),
    ]
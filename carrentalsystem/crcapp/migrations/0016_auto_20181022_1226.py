# Generated by Django 2.1.2 on 2018-10-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcapp', '0015_auto_20181022_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='driverLicenceNumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postCodeAddress',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
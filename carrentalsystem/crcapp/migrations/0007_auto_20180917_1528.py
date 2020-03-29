# Generated by Django 2.1.1 on 2018-09-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcapp', '0006_auto_20180917_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postCodeAddress',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postCodeAddress',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='power',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seatingCapacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='wheelbase',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(),
        ),
    ]
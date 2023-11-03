# Generated by Django 4.2.4 on 2023-11-03 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=100)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('OrganizationID', models.BigIntegerField(default=0)),
                ('CreatedBy', models.BigIntegerField(default=0)),
                ('CreatedDateTime', models.DateField(default=datetime.date.today)),
                ('ModifyBy', models.BigIntegerField(default=0)),
                ('ModifyDateTime', models.DateField(default=datetime.date.today)),
                ('IsDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
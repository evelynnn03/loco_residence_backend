# Generated by Django 4.2.7 on 2024-10-27 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_timeslot_end_time_alter_timeslot_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 10, 28, 1, 23, 24, 794306)),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 10, 28, 1, 23, 24, 794306)),
        ),
    ]
# Generated by Django 5.1 on 2024-09-15 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('bookings', '0002_rename_capacity_facility_total_units'), ('bookings', '0003_remove_facility_facility_type_and_more'), ('bookings', '0004_rename_booking_required_facility_booking_requireds'), ('bookings', '0005_rename_booking_requireds_facility_booking_required'), ('bookings', '0006_alter_booking_resident_alter_booking_section_and_more'), ('bookings', '0007_alter_booking_section')]

    dependencies = [
        ('bookings', '0001_initial'),
        ('users', '0004_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='capacity',
            new_name='total_units',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='facility_type',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='resident',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='total_units',
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='duration',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='facility',
            name='booking_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='end_time',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FacilitySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='bookings.facility')),
            ],
            options={
                'verbose_name_plural': 'Facility Sections',
            },
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='booking',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='bookings.facilitysection'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('section', 'booking_date', 'time_slot')},
        ),
        migrations.DeleteModel(
            name='FacilityType',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='facility',
        ),
        migrations.AlterField(
            model_name='booking',
            name='resident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='users.resident'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='bookings.timeslot'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='bookings.facilitysection'),
        ),
    ]
# Generated by Django 5.1 on 2024-09-15 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_rename_parking_created_at_parking_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parking',
            old_name='parking_updated_at',
            new_name='updated_at',
        ),
    ]
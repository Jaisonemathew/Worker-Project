# Generated by Django 5.0 on 2024-10-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0036_rename_approved_worker_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0 on 2024-08-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0031_remove_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='worker_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Generated by Django 5.0 on 2024-08-17 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0021_customer_address_customer_phno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phno',
            new_name='phone',
        ),
    ]
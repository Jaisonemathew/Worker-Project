# Generated by Django 5.0 on 2024-08-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0019_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
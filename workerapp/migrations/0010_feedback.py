# Generated by Django 3.2.16 on 2023-05-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0009_alter_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phno', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]

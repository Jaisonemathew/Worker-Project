# Generated by Django 3.2.16 on 2023-04-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0003_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('fisrtname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phno', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=25)),
                ('amount', models.TextField()),
                ('worker', models.CharField(max_length=25)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

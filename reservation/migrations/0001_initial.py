# Generated by Django 4.2.7 on 2024-06-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('person', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]

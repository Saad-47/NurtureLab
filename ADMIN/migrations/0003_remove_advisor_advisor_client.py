# Generated by Django 3.2.4 on 2021-11-01 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0002_alter_advisor_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='Advisor_client',
        ),
    ]

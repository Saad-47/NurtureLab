# Generated by Django 3.2.4 on 2021-11-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0003_remove_advisor_advisor_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='Advisor_client',
            field=models.CharField(default='None', max_length=20),
        ),
    ]

# Generated by Django 3.2.25 on 2024-11-12 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0006_jobs_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='Date_Line',
        ),
    ]

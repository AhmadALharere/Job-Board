# Generated by Django 3.2.25 on 2024-11-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='My Plog', max_length=50)),
                ('discription', models.TextField(default='', max_length=1000)),
                ('published_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-23 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='autor',
        ),
    ]

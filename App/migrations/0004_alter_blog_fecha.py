# Generated by Django 4.1.5 on 2023-01-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_blog_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.BooleanField(),
        ),
    ]

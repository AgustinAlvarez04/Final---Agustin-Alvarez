# Generated by Django 4.1.5 on 2023-02-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0008_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='e',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='a',
        ),
    ]

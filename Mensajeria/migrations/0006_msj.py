# Generated by Django 4.1.5 on 2023-02-08 15:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0005_remove_perfil_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=50)),
                ('receptor', models.CharField(max_length=50)),
                ('mensaje', ckeditor.fields.RichTextField(max_length=500)),
            ],
        ),
    ]

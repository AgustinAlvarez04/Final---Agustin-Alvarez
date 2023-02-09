# Generated by Django 4.1.5 on 2023-02-09 14:31

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0006_msj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msj',
            name='remitente',
        ),
        migrations.AddField(
            model_name='msj',
            name='leido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='msj',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

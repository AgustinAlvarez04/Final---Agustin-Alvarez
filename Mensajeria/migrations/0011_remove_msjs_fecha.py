# Generated by Django 4.1.5 on 2023-02-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0010_msjs_delete_e_delete_msj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msjs',
            name='fecha',
        ),
    ]
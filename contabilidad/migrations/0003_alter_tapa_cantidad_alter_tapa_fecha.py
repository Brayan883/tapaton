# Generated by Django 4.0.3 on 2022-04-08 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_rename_equipo_id_detallefondo_equipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapa',
            name='cantidad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tapa',
            name='fecha',
            field=models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro'),
        ),
    ]

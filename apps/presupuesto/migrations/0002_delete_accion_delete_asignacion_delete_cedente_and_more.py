# Generated by Django 5.1.1 on 2024-12-16 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accion',
        ),
        migrations.DeleteModel(
            name='Asignacion',
        ),
        migrations.DeleteModel(
            name='Cedente',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
        migrations.DeleteModel(
            name='Receptor',
        ),
    ]

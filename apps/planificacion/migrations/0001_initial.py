# Generated by Django 5.1.1 on 2024-11-24 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helpers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('fechai', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechaf', models.DateField(verbose_name='Fecha Final')),
                ('objetiv', models.CharField(default='', max_length=64, verbose_name='Objetivos:')),
                ('meta', models.CharField(default='', max_length=64, verbose_name='Meta:')),
            ],
            options={
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('fechai', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechaf', models.DateField(verbose_name='Fecha Final')),
                ('objetiv', models.CharField(default='', max_length=64, verbose_name='Objetivos:')),
                ('meta', models.CharField(default='', max_length=64, verbose_name='Meta:')),
            ],
            options={
                'verbose_name': 'objetivo',
                'verbose_name_plural': 'objetivos',
            },
        ),
        migrations.CreateModel(
            name='Infraestructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('mes', models.CharField(default='', max_length=64, verbose_name='Mes:')),
                ('infraestructura', models.CharField(default='', max_length=64, verbose_name='Infraestrutuctura:')),
                ('cantidad', models.CharField(default='', max_length=64, verbose_name='Cantidad:')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.estado')),
            ],
            options={
                'verbose_name': 'infraestructura',
                'verbose_name_plural': 'infraestructuras',
            },
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('mes', models.CharField(default='', max_length=64, verbose_name='Mes:')),
                ('informativa', models.CharField(default='', max_length=64, verbose_name='Informativa:')),
                ('falsa', models.CharField(default='', max_length=64, verbose_name='Falsa:')),
                ('realesno', models.CharField(default='', max_length=64, verbose_name='Reales no Efectivas:')),
                ('realesf', models.CharField(default='', max_length=64, verbose_name='Reales Efectivas:')),
                ('videop', models.CharField(default='', max_length=64, verbose_name='Video Protección:')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.estado')),
            ],
            options={
                'verbose_name': 'llamada',
                'verbose_name_plural': 'llamadas',
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('mes', models.CharField(default='', max_length=64, verbose_name='Mes:')),
                ('transporte', models.CharField(default='', max_length=64, verbose_name='Transporte:')),
                ('cantidad', models.CharField(default='', max_length=64, verbose_name='Cantidad:')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.estado')),
            ],
            options={
                'verbose_name': 'transporte',
                'verbose_name_plural': 'transportes',
            },
        ),
    ]
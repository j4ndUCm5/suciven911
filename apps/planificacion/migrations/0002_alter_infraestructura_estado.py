# Generated by Django 5.1.1 on 2024-12-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraestructura',
            name='estado',
            field=models.CharField(default='', max_length=64, verbose_name='Estado:'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0003_alter_llamada_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='estado',
            field=models.CharField(default='', max_length=64, verbose_name='Estado:'),
        ),
    ]

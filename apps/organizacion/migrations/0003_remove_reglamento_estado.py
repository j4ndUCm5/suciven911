# Generated by Django 5.1.1 on 2024-12-15 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizacion', '0002_remove_normativa_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reglamento',
            name='estado',
        ),
    ]

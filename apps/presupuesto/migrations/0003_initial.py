# Generated by Django 5.1.1 on 2024-12-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('presupuesto', '0002_delete_accion_delete_asignacion_delete_cedente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombrep', models.CharField(max_length=64, verbose_name='Nombre del Proyecto:')),
                ('fechai', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechac', models.DateField(verbose_name='Fecha de Culminación')),
                ('situacionp', models.CharField(max_length=64, verbose_name='Situación Presupuestaria:')),
                ('montoproyecto', models.CharField(max_length=64, verbose_name='Monto Total del Proyecto:')),
                ('responsableg', models.CharField(max_length=64, verbose_name='Responsable Gerente:')),
                ('responsablet', models.CharField(max_length=64, verbose_name='Responsable Técnico:')),
                ('responsabler', models.CharField(max_length=64, verbose_name='Responsable Registrador:')),
                ('responsablea', models.CharField(max_length=64, verbose_name='Responsable Administrativo:')),
                ('estatus', models.CharField(max_length=64, verbose_name='Estatus del Proyecto:')),
            ],
            options={
                'verbose_name': 'Accion',
                'verbose_name_plural': 'Aacciones',
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombredir', models.CharField(max_length=64, verbose_name='Nombre de la dirección:')),
                ('presuasig', models.CharField(max_length=64, verbose_name='Presupuesto asignado:')),
                ('objeanual', models.CharField(max_length=64, verbose_name='Objetivo general anual:')),
                ('numpartida', models.CharField(max_length=10, verbose_name='Número de partida:')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
        migrations.CreateModel(
            name='Cedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('idc', models.CharField(max_length=100, verbose_name='Id Cedente:')),
                ('partidac', models.CharField(max_length=64, verbose_name='Partida')),
                ('generalc', models.CharField(max_length=64, verbose_name='General')),
                ('espefc', models.CharField(max_length=64, verbose_name='Específicaciones')),
                ('subespefc', models.CharField(max_length=64, verbose_name='Sub-Especialidad')),
                ('denomc', models.CharField(max_length=64, verbose_name='Denomincación')),
                ('presuacorc', models.CharField(max_length=64, verbose_name='Presupuesto acordado')),
                ('caufechac', models.CharField(max_length=64, verbose_name='Causado a la fecha')),
                ('dispc', models.CharField(max_length=64, verbose_name='Disponible a causar')),
                ('montocc', models.CharField(max_length=64, verbose_name='Monto a ceder')),
                ('saldofc', models.CharField(max_length=64, verbose_name='Saldo final')),
                ('direccionc', models.CharField(max_length=64, verbose_name='Dirección cedente')),
            ],
            options={
                'verbose_name': 'Cedente',
                'verbose_name_plural': 'Cedentes',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombrep', models.CharField(max_length=64, verbose_name='Nombre del Proyecto:')),
                ('fechai', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechac', models.DateField(verbose_name='Fecha de Culminación')),
                ('situacionp', models.CharField(max_length=64, verbose_name='Situación Presupuestaria:')),
                ('montoproyecto', models.CharField(max_length=64, verbose_name='Monto Total del Proyecto:')),
                ('responsableg', models.CharField(max_length=64, verbose_name='Responsable Gerente:')),
                ('responsablet', models.CharField(max_length=64, verbose_name='Responsable Técnico:')),
                ('responsabler', models.CharField(max_length=64, verbose_name='Responsable Registrador:')),
                ('responsablea', models.CharField(max_length=64, verbose_name='Responsable Administrativo:')),
                ('estatus', models.CharField(max_length=64, verbose_name='Estatus del Proyecto:')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('idr', models.CharField(default='', max_length=100, verbose_name='Id Receptor:')),
                ('partidar', models.CharField(default='', max_length=64, verbose_name='Partida')),
                ('generalr', models.CharField(default='', max_length=64, verbose_name='General')),
                ('espefr', models.CharField(default='', max_length=64, verbose_name='Específicaciones')),
                ('subespefr', models.CharField(default='', max_length=64, verbose_name='Sub-Especialidad')),
                ('denomr', models.CharField(default='', max_length=64, verbose_name='Denomincación')),
                ('presuacorr', models.CharField(default='', max_length=64, verbose_name='Presupuesto acordado')),
                ('caufechar', models.CharField(default='', max_length=64, verbose_name='Causado a la fecha')),
                ('dispr', models.CharField(default='', max_length=64, verbose_name='Disponible a causar')),
                ('montocr', models.CharField(default='', max_length=64, verbose_name='Monto')),
                ('saldofr', models.CharField(default='', max_length=64, verbose_name='Saldo final')),
                ('direccionr', models.CharField(default='', max_length=64, verbose_name='Dirección receptora')),
            ],
            options={
                'verbose_name': 'Receptor',
                'verbose_name_plural': 'Receptores',
            },
        ),
    ]

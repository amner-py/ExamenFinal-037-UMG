# Generated by Django 3.2.9 on 2021-11-08 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id_tipo_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo de telefono')),
            ],
            options={
                'verbose_name': 'Tipos de teléfono',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('num_telefono', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Número de teléfono')),
                ('predeterminado', models.BooleanField(default=False, verbose_name='Predeterminado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='telefono.tipotelefono', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Telefonos',
            },
        ),
    ]

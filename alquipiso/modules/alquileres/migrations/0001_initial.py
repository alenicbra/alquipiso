# Generated by Django 5.1.3 on 2024-11-12 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Alojamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='alquileres')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alojamientos', to='alquileres.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('fecha_reserva', models.DateField()),
                ('precio_total', models.FloatField()),
                ('pagado', models.BooleanField()),
                ('alojamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquileres.alojamiento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquileres.cliente')),
            ],
        ),
    ]

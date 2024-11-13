# Generated by Django 5.1.3 on 2024-11-13 00:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='propietario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

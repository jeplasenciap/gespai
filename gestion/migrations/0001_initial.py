# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 09:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gestion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Becario',
            fields=[
                ('nombre', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^(?i)([a-z\xf1\xc1\xc9\xcd\xd3\xda\xe1\xe9\xed\xf3\xfa. ]{2,60})$')])),
                ('apellido1', models.CharField(max_length=200)),
                ('apellido2', models.CharField(blank=True, max_length=200)),
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[gestion.models.dni_validator])),
                ('estado', models.CharField(choices=[('A', 'Asignado'), ('S', 'Suplente'), ('R', 'Renuncia'), ('E', 'Excluido'), ('N', 'No asignado')], default='N', max_length=1)),
                ('titulacion', models.CharField(max_length=500)),
                ('horario_asignado', models.CharField(choices=[('M', 'Ma\xf1ana'), ('T', 'Tarde'), ('N', 'No asignado')], default='N', max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.PositiveIntegerField(blank=True, validators=[gestion.models.telefono_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(choices=[('M', 'Ma\xf1ana'), ('T', 'Tarde')], max_length=1)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Centro')),
            ],
        ),
        migrations.AddField(
            model_name='becario',
            name='plaza_asignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.Centro'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gestion.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becario',
            name='plaza_asignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.Plaza'),
        ),
        migrations.AlterField(
            model_name='becario',
            name='telefono',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[gestion.models.telefono_validator]),
        ),
    ]

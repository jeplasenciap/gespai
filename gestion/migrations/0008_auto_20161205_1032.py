# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20161205_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistenciaformacion',
            name='curso',
            field=models.ForeignKey(blank=True, default='Sin curso', on_delete=django.db.models.deletion.CASCADE, to='gestion.PlanFormacion'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_planformacion'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='planformacion',
            unique_together=set([('nombre_curso', 'fecha_imparticion')]),
        ),
    ]
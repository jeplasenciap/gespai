# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20161114_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrelacionBecario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('becario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Becario')),
                ('plaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Plaza')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='prelacionbecario',
            unique_together=set([('becario', 'plaza')]),
        ),
    ]

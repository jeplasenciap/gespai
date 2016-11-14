# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 13:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gestion.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20161114_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsableAula',
            fields=[
                ('nombre', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^(?i)([a-z\xf1\xc1\xc9\xcd\xd3\xda\xe1\xe9\xed\xf3\xfa. ]{2,60})$')])),
                ('apellido1', models.CharField(max_length=200)),
                ('apellido2', models.CharField(blank=True, max_length=200)),
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[gestion.models.dni_validator])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.PositiveIntegerField(blank=True, null=True, validators=[gestion.models.telefono_validator])),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Centro')),
            ],
        ),
    ]
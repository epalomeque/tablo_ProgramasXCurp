# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_programas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cv_prog', models.CharField(max_length=10)),
                ('nombre_prog', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='curp_mas_cvprograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curp', models.CharField(max_length=18)),
                ('cvprograma', models.ForeignKey(to='carga_datos.cat_programas')),
            ],
        ),
    ]

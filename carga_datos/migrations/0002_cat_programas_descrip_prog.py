# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga_datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_programas',
            name='descrip_prog',
            field=models.TextField(default=b'', max_length=255),
        ),
    ]

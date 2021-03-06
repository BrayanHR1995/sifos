# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-04 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecieMunicipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Especie')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Municipio')),
            ],
            options={
                'db_table': 'general_especie_municipio',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0003_auto_20160722_1008'),
        ('configuracion', '0004_auto_20160721_2329'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bocatoma',
        ),
        migrations.DeleteModel(
            name='TipoPresenciaHidrica',
        ),
        migrations.RemoveField(
            model_name='acueducto',
            name='cuenca',
        ),
        migrations.AddField(
            model_name='acueducto',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='configuracion.NivelAcueducto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acueducto',
            name='prestador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='configuracion.Prestador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acueducto',
            name='usuarios',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='microcuenca',
            name='subzona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='configuracion.Subzona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acueducto',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre del Acueducto'),
        ),
        migrations.DeleteModel(
            name='Cuenca',
        ),
    ]

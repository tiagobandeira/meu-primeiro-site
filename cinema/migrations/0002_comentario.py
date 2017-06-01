# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-29 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.PostFilmes')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('nombrevendedor', models.CharField(max_length=30)),
                ('nombrecliente', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Menuplato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='menuplato',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Plato'),
        ),
        migrations.AddField(
            model_name='menu',
            name='platos',
            field=models.ManyToManyField(through='blog.Menuplato', to='blog.Plato'),
        ),
    ]

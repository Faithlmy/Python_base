# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faith',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('system_logo', models.CharField(max_length=100)),
                ('beacon', models.CharField(max_length=100)),
                ('banners', models.TextField()),
                ('info', models.TextField()),
                ('faith_logo', models.CharField(max_length=100)),
                ('myinfo', models.TextField()),
                ('ma_logo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'faith',
            },
        ),
        migrations.CreateModel(
            name='hellomy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'hello',
            },
        ),
    ]

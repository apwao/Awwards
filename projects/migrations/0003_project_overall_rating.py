# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-30 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190630_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='overall_rating',
            field=models.IntegerField(default=0),
        ),
    ]

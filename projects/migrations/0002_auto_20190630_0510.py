# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-30 02:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='usability_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='live_link',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(),
        ),
    ]

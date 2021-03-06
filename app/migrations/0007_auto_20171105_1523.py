# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20171021_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='gravity_enabled',
            field=models.BooleanField(default=False, help_text='Is gravity logging enabled for this beer log?'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When the beer log was initially created'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='device',
            field=models.ForeignKey(help_text='The linked temperature control device from which data is logged', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.BrewPiDevice'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='format',
            field=models.CharField(default='F', help_text='Temperature format to write the logs in', max_length=1),
        ),
        migrations.AlterField(
            model_name='beer',
            name='model_version',
            field=models.IntegerField(default=1, help_text='Version # used for the logged file format'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(db_index=True, help_text='Name of the beer being logged (must be unique)', max_length=255),
        ),
    ]

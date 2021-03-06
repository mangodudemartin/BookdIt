# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookdit', '0004_auto_20160328_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeend',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 13, 0, 34, 552765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='timestart',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 13, 0, 34, 552725, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='timeend',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 13, 0, 34, 553681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='timestart',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 13, 0, 34, 553649, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vendor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2vendor', to='bookdit.vendor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 03:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookdit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestart', models.DateTimeField(default=datetime.datetime(2016, 3, 27, 3, 22, 29, 163548, tzinfo=utc))),
                ('timeend', models.DateTimeField(default=datetime.datetime(2016, 3, 27, 3, 22, 29, 163581, tzinfo=utc))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment2user_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='__default', max_length=255)),
                ('description', models.CharField(default='__default', max_length=4000)),
                ('isActive', models.BooleanField(default=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service2user_supplier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment2service', to='bookdit.service'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment2user_supplier', to=settings.AUTH_USER_MODEL),
        ),
    ]

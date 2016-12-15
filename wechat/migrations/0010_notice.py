# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-14 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0009_myuser_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(null=True)),
                ('fromname', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=256)),
                ('touser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wechat.MyUser')),
            ],
        ),
    ]

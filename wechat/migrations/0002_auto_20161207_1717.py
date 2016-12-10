# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-07 09:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_id', models.CharField(db_index=True, max_length=64, unique=True)),
                ('user_type', models.IntegerField(default=2)),
                ('description', models.CharField(default='', max_length=256)),
                ('phone_num', models.IntegerField(default=0)),
                ('pic_url', models.CharField(default='', max_length=128)),
                ('homepage_url', models.CharField(max_length=128)),
                ('name', models.CharField(default='', max_length=64)),
                ('user_IDnum', models.IntegerField(unique=True)),
                ('registered_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wechat.MyUser'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

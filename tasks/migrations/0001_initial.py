# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-23 23:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[(b'cmd', b'\xe6\x89\xb9\xe9\x87\x8f\xe5\x91\xbd\xe4\xbb\xa4'), (b'file-transfer', b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xbc\xa0\xe8\xbe\x93')], max_length=64)),
                ('content', models.CharField(max_length=255, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x86\x85\xe5\xae\xb9')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'task',
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
                'permissions': (('can_delete_task', '\u53ef\u4ee5\u5220\u9664task'), ('can_view_task', '\u53ef\u4ee5\u67e5\u770btask')),
            },
        ),
        migrations.CreateModel(
            name='TaskLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbb\x93\xe6\x9e\x9c')),
                ('status', models.SmallIntegerField(choices=[(0, b'initialized'), (1, b'sucess'), (2, b'failed'), (3, b'timeout')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Assets')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
            options={
                'db_table': 'tasklogdetail',
                'verbose_name': 'Tasklogdetail',
                'verbose_name_plural': 'Tasklogdetail',
                'permissions': (('can_delete_session', '\u53ef\u4ee5\u5220\u9664tasklog'), ('can_view_session', '\u53ef\u4ee5\u67e5\u770btasklog')),
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-11 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0004_mysql_instance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mysql_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_user', models.CharField(blank=True, max_length=60, null=True)),
                ('db_password', models.CharField(blank=True, max_length=60, null=True)),
                ('privlige', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u6743\u9650')),
                ('dbcluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CMDB.MySQLCluster', verbose_name='\u6240\u5c5e\u96c6\u7fa4')),
            ],
            options={
                'db_table': 'MySQL_User',
                'verbose_name': 'mysql\u5185\u90e8\u7528\u6237',
                'verbose_name_plural': 'mysql\u5185\u90e8\u7528\u6237',
            },
        ),
    ]
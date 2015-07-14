# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('comment', models.CharField(max_length=160, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=80)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=75)),
                ('role', models.CharField(default=b'CU', max_length=2, choices=[(b'SU', b'SuperUser'), (b'DA', b'DeptAdmin'), (b'CU', b'CommonUser')])),
                ('ldap_pwd', models.CharField(max_length=100)),
                ('ssh_key_pwd', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('date_joined', models.DateTimeField(null=True)),
                ('dept', models.ForeignKey(to='juser.DEPT')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('comment', models.CharField(max_length=160, null=True, blank=True)),
                ('dept', models.ForeignKey(to='juser.DEPT')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='juser.UserGroup'),
        ),
    ]

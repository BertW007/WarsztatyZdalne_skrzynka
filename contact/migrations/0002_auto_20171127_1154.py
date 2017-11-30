# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.AddField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(to='contact.Person'),
        ),
    ]
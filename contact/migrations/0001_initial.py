# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('street_number', models.IntegerField()),
                ('home_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
                ('group', models.ManyToManyField(to='contact.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=64, null=True)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NoSeQuePedo', '0015_publicaciones_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicaciones',
            old_name='autor',
            new_name='Email',
        ),
    ]

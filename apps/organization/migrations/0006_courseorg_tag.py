# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-15 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='\u56fd\u5185\u540d\u6821', max_length=10, verbose_name='\u673a\u6784\u6807\u7b7e'),
        ),
    ]

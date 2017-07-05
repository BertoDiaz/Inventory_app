# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170629_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.ForeignKey(blank=True, null=True, to='blog.Order'),
        ),
    ]

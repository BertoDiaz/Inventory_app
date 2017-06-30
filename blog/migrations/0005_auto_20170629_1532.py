# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_order_number_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, to='blog.Product'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170707_1128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buy_Type',
            new_name='Type_of_purchase',
        ),
    ]

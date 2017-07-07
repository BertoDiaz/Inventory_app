# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170707_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Provider',
            new_name='Supplier',
        ),
    ]

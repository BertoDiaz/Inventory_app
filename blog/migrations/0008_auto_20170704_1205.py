# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170704_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='research',
            new_name='researcher',
        ),
    ]

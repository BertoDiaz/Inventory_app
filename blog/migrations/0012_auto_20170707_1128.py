# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170707_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='provider',
            new_name='supplier',
        ),
    ]

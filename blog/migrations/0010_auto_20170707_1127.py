# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170707_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='buy_type',
            new_name='type_of_purchase',
        ),
    ]

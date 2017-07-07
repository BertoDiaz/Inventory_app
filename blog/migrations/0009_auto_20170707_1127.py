# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170704_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='researcher',
            new_name='applicant',
        ),
    ]

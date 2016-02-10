# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portraits',
            name='photo',
            field=models.ImageField(default='pasDimageDispo.png', upload_to='roots/static/images/'),
        ),
    ]

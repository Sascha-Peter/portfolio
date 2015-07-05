# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillcategory',
            name='skill_set',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_category',
            field=models.ForeignKey(default=0, to='skills.SkillCategory'),
            preserve_default=False,
        ),
    ]

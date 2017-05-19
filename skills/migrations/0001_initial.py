# -*- coding: utf-8 -*-
"""Auto generated database migration files."""
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """Migration file for new models."""

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(
                    serialize=False,
                    auto_created=True,
                    primary_key=True, verbose_name='ID'
                )),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_level', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(
                    serialize=False,
                    auto_created=True,
                    primary_key=True,
                    verbose_name='ID'
                )),
                ('category_name', models.CharField(max_length=150)),
                ('skill_set', models.ForeignKey(to='skills.Skill')),
            ],
        ),
    ]

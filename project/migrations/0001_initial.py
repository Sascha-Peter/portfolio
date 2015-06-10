# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('is_live', models.BooleanField(default=False)),
                ('project_title', models.CharField(max_length=250)),
                ('project_description', models.TextField(blank=True)),
                ('project_image', models.ImageField(upload_to='', blank=True)),
                ('project_url', models.URLField(null=True, blank=True)),
                ('last_viewed', models.DateTimeField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]

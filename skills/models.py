"""This file provies all models for the skillset module

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0-alpha
@since: 2015-07-01
"""
from django.db import models


class Skill(models.Model):
    """Class for individual skills"""
    skill_name = models.CharField(max_length=100)
    skill_level = models.TextField(blank=True)
    skill_category = models.ForeignKey('SkillCategory')


class SkillCategory(models.Model):
    """Class for skill categories, grouping skills"""
    category_name = models.CharField(max_length=150)

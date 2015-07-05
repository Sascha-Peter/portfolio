"""This file contains the admin implementation for the admin interface

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0-alpha
@since: 2015-07-01
"""
from django.contrib import admin

from .models import Skill, SkillCategory


class SkillAdmin(admin.ModelAdmin):
    """Model admin for skills"""
    model = Skill


class SkillInline(admin.TabularInline):
    """Inline for skills in skill categories
    @since: 2015-07-05
    """
    model = Skill
    extra = 0


class SkillCategoryAdmin(admin.ModelAdmin):
    """Model admin for skills"""
    model = SkillCategory
    inlines = [SkillInline, ]


admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)

"""This file contains all project related admin definitions

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.0.1-alpha
@since: 2015-05-15
"""
from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    """Model admin for projects"""
    model = Project
    prepopulated_fields = {"slug": ("project_title",)}

admin.site.register(Project, ProjectAdmin)

"""This file contains all views related to skills and skill categories.

author: Sascha Peter <sascha.o.peter@gmail.com>
version:: 0.2.0-alpha
since: 2015-07-05
"""
from django.views.generic.list import ListView

from .models import SkillCategory


class SkillCategoryView(ListView):
    """This view displays the categories."""

    model = SkillCategory

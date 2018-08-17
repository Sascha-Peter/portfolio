"""This file contains all project related test cases.

author: Sascha Peter <sascha.o.peter@gmail.com>
version:: 0.2.0-alpha
since: 2015-05-15
"""
from django.test import TestCase
from django.utils import timezone
from .models import Project

import datetime


class ProjectTextCase(TestCase):
    """Test case for projects."""

    def test_project_is_published(self):
        """Test that a published project is identified correctly."""
        Project.objects.create(project_title="Test1",
                               publication_date="2015-05-14",
                               last_viewed=timezone.now())
        project_one = Project.objects.get(project_title="Test1")
        self.assertEqual(
            project_one.publication_date < datetime.date.today(), True
        )

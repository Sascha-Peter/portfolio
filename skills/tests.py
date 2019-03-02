"""This file contains all tests for the skill module.

author: Sascha Peter <sascha.o.peter@gmail.com>
version:: 0.2.0-alpha
since: 2015-07-05
"""
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from .models import Skill, SkillCategory


class SkillTestCase(TestCase):
    """Test case for Skills."""

    def setUp(self):
        """Setup method."""
        self.factory = RequestFactory()
        self.client = Client()

    def test_list_view(self):
        """Testing if a skill category."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_skill_category_existance(self):
        """Test if skill category exists.

        Test if the skill category which just got added is displayed
        on the homepage.
        """
        SkillCategory.objects.create(category_name="Project Management")
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['object_list']), 1)

    def test_skills_in_category(self):
        """Test if the skills are properly counted."""
        SkillCategory.objects.create(category_name="Development")
        skill_category = SkillCategory.objects.get(category_name="Development")
        Skill.objects.create(
            skill_name="Python", skill_category=skill_category
        )
        Skill.objects.create(
            skill_name="Django", skill_category=skill_category
        )
        response = self.client.get(reverse('home'))
        skills = response.context['object_list'][0]
        skill_set = getattr(skills, 'skill_set')
        self.assertEqual(len(skill_set.all()), 2)

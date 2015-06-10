"""This file defines all project related models

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1-alpha
@since: 2015-05-15
"""
from django.db import models


class Project(models.Model):
    """This class defines the basic project model"""
    creation_date = models.DateField(auto_now=True)
    publication_date = models.DateField(blank=True, null=True)
    is_live = models.BooleanField(default=False)
    project_title = models.CharField(max_length=250)
    project_description = models.TextField(blank=True)
    project_image = models.ImageField(blank=True)
    project_url = models.URLField(blank=True, null=True)
    last_viewed = models.DateTimeField()
    slug = models.SlugField()

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project-detail', kwargs={"slug": self.slug,})

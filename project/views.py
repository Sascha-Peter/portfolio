"""This file contains all views related to the project display.

author: Sascha Peter <sascha.o.peter@gmail.com>
version:: 0.2.0-alpha
since: 2015-05-15
"""
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Project


class ProjectListView(ListView):
    """Generic list view for projects."""

    model = Project

    def get_queryset(self):
        """Custom queryset to return all published projects only."""
        return Project.objects.filter(publication_date__lte=timezone.now())


class ProjectDetailView(DetailView):
    """Generic detail view for a project."""

    model = Project

    def get_object(self):
        """Get object and return."""
        project_object = super(ProjectDetailView, self).get_object()
        project_object.last_viewed = timezone.now()
        project_object.save()
        return project_object

    def get_context_data(self, **kwargs):
        """Get additional context data and return."""
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context["other_projects"] = Project.objects.filter(
            publication_date__lte=timezone.now()
        ).exclude(id=self.object.id)
        return context

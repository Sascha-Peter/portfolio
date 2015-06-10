"""This file contains all views related to the project display

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.0.1-alpha
@since: 2015-05-15
"""
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Project


class ProjectListView(ListView):
    """Generic list view for projects"""
    model = Project

    def get_queryset(self):
        """Custom queryset to return all published projects only"""
        return Project.objects.filter(publication_date__lte=timezone.now())


class ProjectDetailView(DetailView):
    """Generic detail view for a project"""
    model = Project

    def get_object(self):
        object = super(ProjectDetailView, self).get_object()
        object.last_viewed = timezone.now()
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context["other_projects"] = Project.objects.filter(publication_date__lte=timezone.now()).exclude(id=self.object.id)
        return context

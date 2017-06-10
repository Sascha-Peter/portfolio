"""URL definition for project module."""
from django.conf.urls import url
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    url(r'^list/', ProjectListView.as_view(), name="project-list"),
    url(r'^(?P<slug>[-\w]+)/',
        ProjectDetailView.as_view(), name="project-detail"),
]

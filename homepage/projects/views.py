from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Project
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    # context_object_name = 'latest_project_list'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Project.objects.order_by('project_date')

    def get_context_data(self, **kwargs):
        # et = super(IndexView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)

        projects = Project.objects.order_by('project_date')

        context['years'] = [x for x in range(projects.first().project_date.year, projects.last().project_date.year + 1)][::-1]
        return context

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail_context.html'


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
        return Project.objects.order_by('-project_date')

    def get_context_data(self, **kwargs):
        et = super(IndexView, self).get_context_data(**kwargs)

        projects = Project.objects.order_by('-project_date')
        for y in range(projects.first().project_date.year, projects.last().project_date.year + 1):
            et["projects_{0}".format(y)] = projects.filter(project_date__year=y)
        # et['projects_2018'] = projects.filter(project_date__year=2018)
        # et['projects_2017'] = projects.filter(project_date__year=2017)
        return et


# def IndexView(request):
#     projects = Project.objects.order_by('-project_date')
#     projects_by_year = {}
#     for y in range(projects.first().project_date.year, projects.last()project_date.year + 1):
#         projects_by_year[y] = projects.filter(project_date__year=y)
#     context = {
#         'projects_by_year': projects_by_year
#     }
#     return render(request, 'projects/index-old.html', context)


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

#
# def index(request):
#     latest_project_list = Project.objects.order_by('-project_date')[:5]
#     context = {
#         'latest_project_list': latest_project_list,
#     }
#     return render(request, 'projects/index-old.html', context)
#
# def detail(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     context = {
#         'project': project,
#     }
#     return render(request, 'projects/detail.html', )
#


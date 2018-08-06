from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Project
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        return Project.objects.order_by('-project_date')[:5]

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

#
# def index(request):
#     latest_project_list = Project.objects.order_by('-project_date')[:5]
#     context = {
#         'latest_project_list': latest_project_list,
#     }
#     return render(request, 'projects/index.html', context)
#
# def detail(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     context = {
#         'project': project,
#     }
#     return render(request, 'projects/detail.html', )
#


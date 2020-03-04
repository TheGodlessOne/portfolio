from django.shortcuts import render
from django.http import HttpResponse
from responce.models import Project


# Create your views here.
def project_all(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

def project_detail(request, p_key):
    project = Project.objects.get(p_key=p_key)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from responce.models import Project


# Create your views here.
def index(request): 
    return render(request, 'index.html')

def project_all(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

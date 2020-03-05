from django.shortcuts import render
from django.http import HttpResponse
from responce.models import Project
from responce.forms import Responce
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect


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

@cache_page(60 * 15)
@csrf_protect
def contact_form(request):
    if request.method == 'POST':
        form = Responce(request.POST)
        if form.is_valid():
            name = form.fields['name']
            email = form.fields['email']
            site_url = form.fields['site_url']
            comment = form.fields['comment']
            instances = form.save()
            return render(request, 'contacts.html', {'form': form})
    else:
        form = Responce()
    return render(request, 'contacts.html', {'form': form})

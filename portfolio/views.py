from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    projects = models.Project.objects.all()
    return render(request, 'portfolio/home.html', context={'projects' : projects})

def certificates(request):
    certificates_ = models.Certificate.objects.all()
    return render(request, 'portfolio/certificates.html', context={'certificates' : certificates_})

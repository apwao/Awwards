from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProjectForm
from .models import Project


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application together
    with the navigation bar to help sign up and log into the application
    """
    
    return render(request, 'homepage.html')

def upload_project(request):
    """
    upload_project view function that presents a form to the user for
    providing details about their project and uploading them onto the application 
    for vetting
    """
    project_form=ProjectForm
    return render(request, 'upload_project.html', {'project_form':project_form})
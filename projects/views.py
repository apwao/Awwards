from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProjectForm
from .models import Project
from rating.models import Rating
from rating.forms import RatingForm
from django.contrib.auth.decorators import login_required
from rating.views import rate_project,rate_form
from rating import *


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application together
    with the navigation bar to help sign up and log into the application
    """
    
    return render(request, 'homepage.html')

@login_required(login_url='/accounts/login/')
def upload_project(request):
    """
    upload_project view function that presents a form to the user for
    providing details about their project and uploading them onto the application 
    for vetting
    """
    current_user = request.user
    current_user_name = current_user.username
    # project_ratings=Rating.objects.filter(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project_post = form.save(commit=True)  
        else:
            raise Http404 
            
        return redirect(view_projects)
    else:   
        project_form=ProjectForm()
        
    return render(request, 'upload_project.html', {'project_form':project_form})

@login_required(login_url='/accounts/login/')
def view_projects(request):
    """
    view_project view function to display the projects after the user 
    submits their project plus all other projects uploaded by other users
    """
    current_user=request.user
    current_user_name=current_user.username
    projects=Project.objects.all()
    return render(request, 'view_projects.html',{'projects':projects, 'current_user_name':current_user})

@login_required(login_url='/accounts/login/')
def single_project(request,project_id):
    """
    single_project view function to display the details of a single project and display a form to
    submit a vote for the project
    """
    
    project=Project.objects.get(id=project_id)
    
    
    
    return render(request, 'single_project.html',{'project':project})


@login_required(login_url='/accounts/login/')
def vote(request):
    """
    vote view function to process the input from the vote form and return the average vote
    """
    overall_vote = rate_project()

    
    return render(request, 'rateform.html')
    
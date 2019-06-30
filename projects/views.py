from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    """
    homepage view function to display the landing page of the application together
    with the navigation bar to help sign up and log into the application
    """
    
    return render(request, 'homepage.html')
@login_required(login_url='/accounts/login')
def upload_project(request):
    """
    upload_project view function that presents a form to the user for
    providing details about their project and uploading them onto the application 
    for vetting
    """
    print('hello')
    current_user = request.user
    print(current_user)
    current_user_name = current_user.username
    print(current_user_name)
    if request.method == 'POST':
        print('True')
        form = ProjectForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('---' * 30)
            print('True')
            project_post = form.save(commit=True)
            print('**' * 20)
            print(project_post)
        return redirect('view_projects')
    else:   
        project_form=ProjectForm()
        
    return render(request, 'upload_project.html', {'project_form':project_form,"current_user_name":current_user_name})

@login_required(login_url='/accounts/login')
def view_projects(request):
    """
    view_project view function to display the projects after the user 
    submits their project plus all other projects uploaded by other users
    """
    current_user=request.user
    current_user_name=current_user.username
    projects=Project.objects.all()
    return render(request, 'view_projects.html',{'projects':projects, 'current_user_name':current_user})
    
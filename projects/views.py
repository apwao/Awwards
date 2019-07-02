from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProjectForm
from .models import Project
from rating.models import Rating
from rating.forms import RatingForm
from django.contrib.auth.decorators import login_required
from rating.views import rate_project,rate_form
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Project
from .serializer import ProjectSerializer
from rest_framework import status



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
    # get all ratings for a specific project
    all_ratings=Rating.objects.filter(project_id=project)
    average_rates=[]
    overall_final_rating=0
        
    for rating in all_ratings:
        average_rates.append(rating.average_vote)
            
    final_rates=sum(average_rates)
    if len(all_ratings)>0:
        overall_rating=final_rates/len(all_ratings)
        overall_final_rating=overall_rating
    else:
        overall_rating=0
        overall_final_rating=overall_rating  
    
    return render(request, 'single_project.html',{'project':project,'overall_final_rating':overall_final_rating})


def search(request):
    """
    search function to search the database using a search term
    and return the project.
    """
    if 'find_project' in request.GET and request.GET['find_project']:
        project_name=request.GET.get('find_project')
        
        searched_project=Project.search_project(project_name)
        
    return render(request,'search_results.html',{'searched_project':searched_project})  

class ProjectList(APIView):
    """
    """
    def get(self,request, format=None):
        """
        method get to perform GET operations
        """
        all_projects=Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
    
    def post(self, request, formal=None):
        """
        method post used to perform POST operations
        """
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
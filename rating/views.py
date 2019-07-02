from django.shortcuts import render,redirect
from .models import Rating
from django.contrib.auth.decorators import login_required
from projects.models import Project
from django.contrib.auth.models import User
from .forms import RatingForm
from django.http  import HttpResponse






# Create your views here.
@login_required(login_url='/accounts/login')
def rate_form(request, id):
    """
    rate_form view function to display the rating form to the user
    """
    # get project to be rated from the DB
    project=Project.objects.get(id=id)
    current_user = request.user
    # get all the ratings associated with that project from the ratings table
    ratings=Rating.objects.filter(project_id=project.id)
    # create a rating form and pass it the request values of the post method
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
        
            # save the form in a variable instead of sending directly to db
            user_rating = form.save(commit=False)
            
            # Fixing values for the other fields in the rating model that 
            # don't come from the user
            user_rating.average_vote=round((user_rating.usability_vote + user_rating.content_vote + user_rating.design_vote)/3)
            print('-' * 30)
            print(project.id)
            user_rating.project_id=project
            
            user_rating.voter_id=current_user
            
            user_rating.save()
            return redirect('view_projects')
    else: 
        rateform=RatingForm()
    
    return render(request, 'rateform.html', {'rateform':rateform, 'project':project})

@login_required(login_url='/accounts/login')
def rate_project(request, project_id):
    """
    rate_project view function to process the user input rating information
    based on usability,content and design and return an average
    rating which will be stored in the database
    """
    current_user=request.user
    
    # get project to be rated from the DB
    project=Project.objects.get(id=project_id)
    # get all the ratings associated with that project from the ratings table
    ratings=Rating.objects.filter(project_id=project.id)
    # create a rating form and pass it the request values of the post method
    form = RatingForm(request.POST)
    
    # Validating of the form to check if all the values passed are valid for those fields
    if form.is_valid():
        
        # save the form in a variable instead of sending directly to db
        user_rating = form.save(commit=False)
        
        # Fixing values for the other fields in the rating model that 
        # don't come from the user
        user_rating.average_vote=round((user_rating.usability_vote + user_rating.content_vote + user_rating.design_vote)/3,2)
        print('-' * 30)
        print(project.id)
        user_rating.project_id=project
        
        user_rating.voter_id=current_user
        
        # user_rating.save()
        return redirect('view_projects')
    else:
        rateform=RatingForm()
        
    return HttpResponse('Your vote has been submitted!')
        
    # return render(request, 'rateform.html',{'rateform':rateform})

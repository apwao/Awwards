from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.
class Project(models.Model):
    """
    class Project to create instances of projects uploaded to the site
    """
    
    project_title=models.CharField(max_length=200)
    project_image=models.ImageField(upload_to='projects/')
    project_description=HTMLField()
    live_link=URLOrRelativeURLField()
    upload_date=models.DateTimeField(auto_now_add=True)
    posted_by=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    usability_rating=models.IntegerField(default=0)
    design_rating=models.IntegerField(default=0)
    content_rating=models.IntegerField(default=0)  
    posted_by=models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    
    
    def save_project(self):
        """
        save project method to save project details provided 
        by the user to the database
        """
        self.save()
        
    def delete_project(self):
        """
        delete_project method to remove a project from the database
        """
        self.delete()
        
    def update_project(self):
        """
        update_project method to replace details of a given
        project in the database with new ones
        """
        self.update()
        
    
    def __str__(self):
        return self.name      
        
            

    
    
    
from django.db import models
from projects.models import Project
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Rating(models.Model):
    """
    Class Rating to enable creation of a project's overall rating
    based on the usability rating, content rating and design rating
    """
    
    usability_vote=models.IntegerField()
    design_vote=models.IntegerField()
    content_vote=models.IntegerField()
    average_vote=models.FloatField()
    project_id=models.ForeignKey(Project)
    voter_id=models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def save_rating(self):
        """
        save_rating method to add a rating to the database
        """
        self.save()
        
    def delete_rating(self):
        """
        delete_rating method to remove a rating from the database
        """
        self.delete()
        
    def update_rating(self):
        """
        update_rating method to replace an existing rating and its details 
        in the database with new ones
        """
        self.update()
        
   
    def __str__(self):
        return self.name
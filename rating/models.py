from django.db import models
from projects.models import Project


# Create your models here.
class Rating(models.Model):
    """
    Class Rating to enable creation of a project's overall rating
    based on the usability rating, content rating and design rating
    """
    
    usability_vote=models.IntegerField(default=o)
    design_vote=models.IntegerField(default=o)
    content_vote=models.IntegerField(default=o)
    average_vote=models.IntegerField(default=o)
    project_id=models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    

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
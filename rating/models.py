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
    

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    """
    class Project to create instances of projects uploaded to the site
    """
    
    project_title=models.CharField(max_length=200)
    project_image=models.ImageField(upload_to='projects/')
    project_description=HTMLField()
    live_link=models.URLField()
    upload_date=models.DateTimeField(auto_now_add=True)
    
    
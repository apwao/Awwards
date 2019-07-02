from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Class profile serializers to convert the Profile django model into a JSON object
    """
    class Meta:
        model=Project
        fields=('project_title','project_image','project_description','live_link','posted_by')

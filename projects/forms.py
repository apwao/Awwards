from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    """
    Class ProjectForm to help obtain input from the user on their
    project-title, landing-page-image, project-description and a live link to
    the actual project. This class provides a way to obtain this input from the user
    based on the Project class.
    """
    class Meta:
        model=Project
        fields=('project_title','project_image','project_description','live_link')
        exclude=['upload_date']
        
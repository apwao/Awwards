from .models import Rating
from django import forms

class RatingForm(forms.ModelForm):
    """
    class RatingForm to help take user input on rates and save 
    them to the database
    """
    class Meta:
        model=Rating
        fields=('usability_vote','design_vote','content_vote')
        exclude=['average_vote','project_id']
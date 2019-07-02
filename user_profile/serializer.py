from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Class profile serializers to convert the Profile django model into a JSON object
    """
    class Meta:
        model=Profile
        fields=('bio','profile_photo')
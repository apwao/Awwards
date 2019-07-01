from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    Class Pofile to create an instance of a user profile
    """
    bio=models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    user_id = models.IntegerField(default=0)
    
    def save_profile(self):
        """
        save_image method to check whether an instance of image
        is successfully stored to the database
        """
        self.save()
        
    def delete_profile(self):
        """
        delete_profile method to remove a profile from the database
        """
        self.delete()
        
    def update_profile(self):
        """
        update_profile method to replace a profile and its details in the database
        """
        self.update()
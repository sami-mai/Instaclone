from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

'''
Profile model class
'''


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    bio = HTMLField()
    profile_name = models.ForeignKey(User)

    def __str__(self):
        return self.name

    '''
    Class method that allows us to search for a user using their profile name.
    '''
    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(name__icontains=search_term)
        return profile


'''
Image model class
'''


class Image(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True)
    image_name = models.CharField(max_length=60)
    image_caption = HTMLField()
    profile_name = models.ForeignKey(Profile)
    Likes = models.CharField(max_length=60)
    Comments = models.CharField(max_length=60)

    def __str__(self):
        return self.image_name

    '''
    Save an image to database.
    '''
    def save_image(self):
        self.save()

    '''
    Delete image from database.
    '''
    def delete_image(self):
        self.delete()

    '''
    Class method to Update image caption in database.
    '''
    @classmethod
    def update_caption(cls):
        pass

    '''
    Class method that Allows us to get a image using a its ID.
    '''
    @classmethod
    def get_image_by_id(cls, id):
        pass
